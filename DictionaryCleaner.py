# Diarmuid Byrne
# G00302711
# 10/03/2016

import re

f = open('words.txt', 'r')
outFile = open('CleanedDictionary.txt', 'w')
dictList = []
sub9List = []


def appendFile(fileName):
    gsl = open(fileName, 'r+')
    global sub9List, dictList
    # Remove digits, space and newline characters
    for line in gsl:
        regex = re.compile('[^a-zA-Z]')
        result = regex.sub('', line)
        result = result.strip()
        if len(result) < 9 and len(result) >= 3:
            sub9List.append(result)
        if len(result) == 9:
            dictList.append(result)

# Write results to file
def writeToFile(dictSet, sub9Set):
    # Print 9 letter words first to speed up searching
    for word in dictSet:
        word = word.upper()
        outFile.write(word+'\n')
    # Print all other words sub 9 letters
    for word in sub9Set:
        word = word.upper()
        outFile.write(word+'\n')

# Remove everything already in file
outFile.seek(0,0)
outFile.truncate()

# Add all words from multiple wordlists with 9 letters and under to a list
appendFile('Dictionary.txt')
appendFile('gsl.txt')
appendFile('OxfordDictionary.txt')

# Remove duplicate entries from the dictionary
dictSet = set(dictList)
sub9Set = set(sub9List)
#Write results to file
writeToFile(dictSet, sub9Set)
