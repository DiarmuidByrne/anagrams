# Diarmuid Byrne
# G00302711
# 12/03/2016
import random
import time
f = open('wordlist.txt', 'r')

# Dictionaries for vowels and consonants
# Here, the letters serve as the keys and their corresponding values
# are the weight of each letter
# Weighting based off scrabble tile frequencies found here:
# http://deadspin.com/5975490/h-y-and-z-as-concealed-weapons-we-apply-google-inspired-math-to-scrabbles-flawed-points-system
vowels = {'a':9,'e':12,'i':9,'o':8,'u':4}
consonants = {'b':2,'c':2,'d':4,'f':2,'g':3,'h':2,'j':1,'k':1,'l':4,'m':2,'n':6,'p':2,'q':1,'r':6,'s':4,'t':6,'v':2,'w':2,'x':1,'y':2,'z':1}

# Removes newline character from each line
words = [line.rstrip() for line in f]

# Generates a random anagram 9 letters long.
# The anagram uses the weighted letters in the vowel and consonant dictionaries defined above
# Code Exerpt from: http://stackoverflow.com/questions/2570690/python-algorithm-to-randomly-select-a-key-based-on-proportionality-weight
def weightedPick(d):
    r = random.uniform(0, sum(d.values()))
    s = 0.0
    for k, w in d.items():
        s += w
        if r < s: return k
    return k

# Creates an anagram ensuring there are at least 3 vowels and 4 consonants.
def randomAnagram():
    anagram = []
    consCount = vowelCount = 0
    # Add new letter until the anagram reaches the desired length
    while len(anagram) < 9:
        nextChar = random.randint(0, 1)
        # Add consonant
        if(nextChar == 0 and consCount < 7):
            anagram.append(weightedPick(consonants).upper())
            consCount += 1
        # Add vowel
        elif(nextChar == 1 and vowelCount < 4):
            anagram.append(weightedPick(vowels).upper())
            vowelCount += 1
    return anagram

def solve(anagram):
    # Keeps a tally of the closest match until an
    # exact anagram is found or the end of the file is reached
    bestResult = ""
    # Skip loop if current best result is longer than the word
    for word in words:
        if(len(bestResult) == len(anagram)):
            return bestResult
        elif(len(bestResult) >= len(word)):
            continue
        if "".join(sorted(word)) in "".join(sorted(anagram)):
            if len(word) > len(bestResult):
                bestResult = word
            elif len(bestResult) == len(anagram):
                return bestResult
    return bestResult

#Randomize 9 letter word to test the conundrum
anagram = randomAnagram()
# Solve the anagram
result = solve(anagram)# Print out the anagram as a single string and its result
print("Anagram:", "".join(anagram))
print("Result:", result)

# Measures the time complexity of the script.
# Timeit.timeit has been used over time.time, as it executes the code multiple times
# to account for other processes that might affect the result
if __name__ == '__main__':
    import timeit
    numLoops = 5
    time = timeit.timeit("mainOne(randomAnagram())", setup="from __main__ import solve, randomAnagram", number=numLoops)
    print(time)
    print(numLoops, "Loops, Average of",  time/numLoops, "seconds per loop" )
