# Donia & Samantha

story = "alice.txt"
f = open(story, 'r')

contents = f.read();
contents = contents.split(" ")
contents = [x.strip('\n') for x in contents]
contents = [x.strip(',') for x in contents]

print contents

def counter(word):
    reduce ((lambda x: x), word) 

listOfWords = ["hello", "hello", "hi", "bye", "hello"]

c = 0;
def counting(word):
    for x in listOfWords:
        if(x == word):
            c += 1;
    return c
