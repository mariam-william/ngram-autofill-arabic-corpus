# -*- coding: utf-8 -*-
"""
@authors: Alaa Farouk - Mariam Makram
"""

import re
from tkinter import *
import tkinter as tk
ngramsNum = 3
ngrams_list = {}
probabilities = {}
count = 0
nPredictions = 5
options=[]

def prepareData():
    file = open("ds.txt","r", encoding="UTF-8")
    dataset = file.read()
    file.close()
    return dataset

# preparing data for generating ngrams
def tokenizeText(text):
    text = text.lower()
    # tokenizing text to work on arabic and english words and numbers
    text = re.sub('[^\sa-zA-Z0-9ء-ي]', '', text)
    return text.split()


def generateNGrams(words_list, n, count = 0):
    for num in range(0, len(words_list)):
        sentence = ' '.join(words_list[num:num + n])
        if sentence not in ngrams_list.keys():
            ngrams_list[sentence] = 1
        else:
            ngrams_list[sentence] += 1
        count += 1
        probabilities[sentence] = ngrams_list[sentence] / count


def splitSequence(seq):
    sequence = seq.split(" ")
    return sequence


def getPredictions(sequence, nPredictions):
    predicted = []
    inputSequence = splitSequence(sequence)
    for sentence in probabilities.keys():
        if sequence in sentence:
            outputSequence = splitSequence(sentence)
            if outputSequence[0] != inputSequence[0] or outputSequence[1] != inputSequence[1]:
                continue
            predicted.append((sentence, probabilities[sentence]))

    predicted.sort(key=lambda x: x[1], reverse=True)

    if len(predicted) < nPredictions:
        nPredictions = len(predicted)
    print(len(predicted))
    for i in range(0, nPredictions):
        outputSequence = predicted[i][0].split(" ")
        print(outputSequence[2])
        options.append(outputSequence[2])
    return options 
        


dataset = prepareData()
words = tokenizeText(dataset)
generateNGrams(words, 3)

# for seq in probabilities:
#    print(seq, probabilities[seq])
'''
seq = input("Enter two words: ")
getPredictions(seq.lower(), nPredictions)
'''


  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing input
inputuser_var=tk.StringVar()
 
  
# defining a function that will get the name and password and print them on the screen
outputoptions=[]
# declaring string variable for storing input
inputuser_var=tk.StringVar()

# defining a function that will get the words and print them on the screen
def Searchbutton():
    inputuser=inputuser_var.get()
   # print("Two Words: " + inputuser.lower())
    outputoptions=getPredictions(inputuser.lower(), nPredictions)
    mb=  Menubutton ( root, text="Auto fill for the words", relief=RAISED )
    mb.grid(row=3,column=1)
    mb.menu =  Menu (mb, tearoff = 0 )
    mb["menu"] =  mb.menu
    mayoVar = IntVar()    
    for i in range(0, len(outputoptions)):
         mb.menu.add_checkbutton ( label=inputuser+" " + str(outputoptions[i]), variable=mayoVar )
    
   
     
# creating a label for input using widget Label
words_label = tk.Label(root, text = 'Enter Two Words : ', font=('calibre',10, 'bold'))
  
# creating a entry for input words using widget Entry
words_entry = tk.Entry(root,textvariable = inputuser_var, font=('calibre',10,'normal'))
   

# creating a button using the widget Button that will call the search function
s_btn=tk.Button(root,text = 'Submit', command = Searchbutton)

#placing the label and entry in the required position using grid method
words_label.grid(row=0,column=0)
words_entry.grid(row=0,column=1)
s_btn.grid(row=2,column=1)
# performing an infinite loop for the window to display
root.mainloop()

