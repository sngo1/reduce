#OfTheAbsurd (Donia Tung & Samantha Ngo)
# SoftDev2 pd7
# K18 -- Reductio ad Absurdum
# 2018-04-30
from functools import reduce


story = "alice.txt"
f = open(story, 'r')

contents = f.read().split();
contents = [x.strip('\n') for x in contents]
contents = [x.strip(',') for x in contents]

#print contents

def counter(word, file):
    list = [1 for x in file if x == word]
    if list == []:
        return 0
    return reduce ((lambda x, y: x + y), list)

test = "hi there this here sentence is the test sentence so it is here so that there is a sentence for testing".split()

print counter("is", test) #3
print counter("here", test) #2

def countGroup(group, file):
    return true

def mostFrequent(file):
    wordfreq = [(counter(x, file), x) for x in file]
    return "Word: " + max(wordfreq)[1] + " Frequency: " + str(max(wordfreq)[0])

print mostFrequent(test)
