# -*- coding: utf-8 -*-
"""

@authors: Alaa Farouk - Mariam Makram
"""

import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox

ngramsNum = 3
ngrams_list = {}
probabilities = {}
count = 0
nPredictions = 5
options = []


def prepareData():
    file = open(
        "dataset.txt",
        "r", encoding="UTF-8")
    dataset = file.read()
    file.close()
    return dataset


# preparing data for generating ngrams
def tokenizeText(text):
    text = text.lower()
    # tokenizing text to work on arabic and english words and numbers
    text = re.sub('[^\sa-zA-Z0-9ء-ي]', '', text)
    return text.split()


def calculateProb(sentence, counter=0):
    if sentence not in ngrams_list.keys():
        ngrams_list[sentence] = 1
    else:
        ngrams_list[sentence] += 1
    counter += 1
    probabilities[sentence] = ngrams_list[sentence] / counter


def generateNGrams(words_list, n, counter=0):
    nGrams = []
    for num in range(0, len(words_list)):
        sentence = ' '.join(words_list[num:num + n])
        calculateProb(sentence, counter)

def splitSequence(seq):
    return seq.split(" ")


def getPredictions(sequence):
    predicted = []
    nPred = nPredictions
    inputSequence = splitSequence(sequence)
    for sentence in probabilities.keys():
        if sequence in sentence:
            outputSequence = splitSequence(sentence)
            cont = False
            for i in range(0, len(inputSequence)):
                if outputSequence[i] != inputSequence[i]:
                    cont = True
                    break
            if cont:
                continue
            predicted.append((sentence, probabilities[sentence]))
    predicted.sort(key=lambda x: x[1], reverse=True)

    noPrediction = False
    if len(predicted) == 0:
        noPrediction = True
    else:
        if len(predicted) < nPredictions:
            nPred = len(predicted)

        for i in range(0, nPred):
            outputSequence = predicted[i][0].split(" ")
            options.append(outputSequence[len(inputSequence)])
    return options, noPrediction, nPred


def popup():
    messagebox.showinfo("Autofill Alert", "No predicted words")

# defining a function that will get the words and print them on the screen
def searchToken():
    userInput = userInput_var.get()
    generateNGrams(words, len(splitSequence(userInput)) + 1, count)
    output_options, noPredictions, nPred = getPredictions(userInput.lower())
    mb = Menubutton(root, text="Auto fill for the words", relief=RAISED)
    mb.grid(row=3, column=1)
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    mayoVar = IntVar()
    if noPredictions:
        popup()
    else:
        for i in range(0, nPred):
            mb.menu.add_checkbutton(label=userInput + " " + str(output_options[i]))


dataset = prepareData()
words = tokenizeText(dataset)

root = tk.Tk()
root.geometry("400x400")
root.title("AutoFill Arabic Corpus n-gram")

output_options = []
userInput_var = tk.StringVar()



words_label = tk.Label(root, text=('Enter search words: '), fg=('indigo'), font=('AR CENA', 14, 'bold'))

words_entry = tk.Entry(root, textvariable=userInput_var, font=('AR CENA', 10, 'normal'))

searchButton = tk.Button(root, text='Submit', command=searchToken)

# placing the label and entry in the required position using grid method
words_label.grid(row=0, column=0)
words_entry.grid(row=0, column=1)
searchButton.grid(row=2, column=1)
# performing an infinite loop for the window to display
root.mainloop()
