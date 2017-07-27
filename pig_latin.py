#-------------------------------------------------------------------------------
# Name:        Pig Latin Translator
# Purpose:
#
# Author:      Jorge
#
# Created:     19/03/2014
# Copyright:   (c) Jorge 2014
# Licence:     <XXXXXXXXXXXXX>
#-------------------------------------------------------------------------------
print ('Welcome to the Pig Latin Translator!')

name = input("What is your name: ")
pyg = "ous"
original = name

if len(original) > 0 and name.isalpha():
    print ("OK, Your name in Pig Latin is " + name)
    word = original.lower()
    first = word[0]
    new_word = word+first+pyg
    new_word = new_word[1:]
    print ("Your name in Pig Latin is " + new_word + "!!!")
else:
    print("Please use your name!!!")