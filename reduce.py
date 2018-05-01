#OfTheAbsurd (Donia Tung & Samantha Ngo)
# SoftDev2 pd7
# K18 -- Reductio ad Absurdum
# 2018-04-30

from functools import reduce

# Read in contents -------------------------------------------------------------------------------------------------------------------------------------------
story = "alice.txt"
f = open(story, 'r')

contents = f.read().split();
contents = [x.strip('\n') for x in contents]
contents = [x.strip(',') for x in contents]

#print contents

# Count frequency of a single word ---------------------------------------------------------------------------------------------------------------------------
def counter(word, file):
    list = [1 for x in file if x == word]
    if list == []:
        return 0
    return reduce ((lambda x, y: x + y), list)

test = "hi there this here sentence is the test sentence so it is here so that there is a sentence for testing".split()

print counter("is", test) #3
print counter("here", test) #2

# Find frequency of a group of words(phrase) ----------------------------------------------------------------------------------------------------------------
def frequencyOfGroup(word_list):
    freq = 0;
    print "GROUP FREQ: ", [counter(x, contents) for x in word_list]

print frequencyOfGroup(['the','Alice'])
print "=============================="

def addedGroupFreq(word_list):
    freq = [counter(x, contents) for x in word_list]
    print "GROUP FREQ: ", freq
    return reduce((lambda x,y : x+y), freq)

print addedGroupFreq(['the','Alice'])
print "=============================="

# Find most frequent word (takes a long time) ----------------------------------------------------------------------------------------------------------------
def countGroup(group, file):
    return true

def mostFrequent(file):
    wordfreq = [(counter(x, file), x) for x in file]
    return "Most Frequent Word: '" + max(wordfreq)[1] + "' appears " + str(max(wordfreq)[0]) + " times."

print mostFrequent(test)
print "TEST BOOK:"
#print mostFrequent(contents)
