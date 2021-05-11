# -*- coding: utf-8 -*-
"""

@authors: Alaa Farouk - Mariam Makram
"""

import re

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
        print("No predicted words")
        noPrediction = True
    else:
        if len(predicted) < nPredictions:
            nPred = len(predicted)

        for i in range(0, nPred):
            outputSequence = predicted[i][0].split(" ")
            print(outputSequence[len(inputSequence)])
            options.append(outputSequence[len(inputSequence)])
    return options, noPrediction, nPred


dataset = prepareData()
words = tokenizeText(dataset)

seq = input("Enter search words: ")
generateNGrams(words, len(splitSequence(seq)) + 1, count)
getPredictions(seq.lower())
