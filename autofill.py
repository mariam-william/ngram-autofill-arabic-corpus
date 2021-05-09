# -*- coding: utf-8 -*-
"""
@authors: Alaa Farouk - Mariam Makram
"""

ngramsNum = 3
ngrams_list = {}
probabilities = {}
count = 0
nPredictions = 3

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
    text = text.replace(',', ' ')
    text = text.replace('/', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('.', ' ')
    text = text.replace('،', '')
    text = text.replace('\'', '')
    text = text.replace('\n', ' ')
    return text.split()


def generateNGrams(words_list, n, count = 0):
    for num in range(0, len(words_list)):
        sentence = ' '.join(words_list[num:num + n])
        return sentence

dataset = prepareData()
words = tokenizeText(dataset)
sentence = generateNGrams(words, ngramsNum)

for seq in probabilities:
    print(seq, probabilities[seq])

