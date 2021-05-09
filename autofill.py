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

def prepareData():
    file = open(
        "D:\\College\\Level_4\\Second_Semester\\Natural Language Processing\\Assignments\\Assignment_1\\NGram_Autofill\\ds.txt",
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


dataset = prepareData()
words = tokenizeText(dataset)
generateNGrams(words, 3)

# for seq in probabilities:
#    print(seq, probabilities[seq])

seq = input("Enter two words: ")
getPredictions(seq.lower(), nPredictions)

