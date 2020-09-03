# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:53:50 2020

@author: admin
"""

import csv
#racial slur set to compare individual words with.
racial_slur = {"slur1",
               "slur2",
               "slur3",
               "slur4",
               "slur5"}
#temporarily store flagged words in a comment
flagged_words = []


#-----------HELPER FUNCTION---------------------------
def calculate_degree(comment_string):
    #split the comment based on spaces
    sentence = comment_string.split()
    slur_count = 0
    #for each word in the comment
    for word in sentence:
        #lowercase to check if it's a slur
        word.lower()
        #remove all non alphabets from word and compare it with slurs set
        formatted_word = ''.join(filter(str.isalnum, word))
        if formatted_word in racial_slur:
            flagged_words.append(formatted_word)
            #inc slur count if the word is a slur
            slur_count = slur_count + 1
    #return total number of slurs in a comment
    if slur_count == 0: return 0
    return round(slur_count/len(sentence)*100, 2)
#----------END HELPER FUNCTION------------------------



#------------DRIVER CODE------------------------------
#create a file to store all profanity degrees
output_file = open("profanity_degree.txt", "w")
output_file.write("index - instaID - profanity% - found words \n")
#open comments file
with open('insta.csv','r') as comments_file:
    index = 1
    #get all the file rows and ignore commas in comments
    comments = csv.reader(comments_file, skipinitialspace=True)
    #for each row compare the comment to the racial slur set
    for row in comments:
        #get degree of slurs for each comment (3rd column)
        degree = calculate_degree(row[2])
        #if no slurs are present write 0% to output file
        if degree == 0:
            # format string to copy to output file
            temp_line = ""+ str(index) + " - " + row[1] + " - " + str(degree) + "%" + " - None \n"
            output_file.write(temp_line)
        #if more than 0 slurs is present write % to output file
        else:
            #string to store all the slurs present in the comment
            word_list = ""
            for slur in flagged_words:
                word_list = word_list + slur + ", "
            #reset slur word list
            flagged_words = []
            #format string to copy to output file
            temp_line = ""+ str(index) + " - " + row[1] + " - " + str(degree) + "%" + " - " + word_list[:-2] +"\n"
            output_file.write(temp_line)
        #increment index for output file
        index = index + 1


output_file.close()

