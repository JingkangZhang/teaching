## 1. rewrite: in functions
from random import choice
name = input("Input file name: ")  ## optional: loop
## 1.1. try.. except check file exists
flag = 0
while flag == 0 :
    try :
        fhand = open(name)
        print(fhand)
        flag = 1
    except :
        name = input("Can't find the file, please enter the file name again: ")


N = int(input("How may grams: "))
## 2. N-gram instead of 3
fileList = open(name).read().split()
d = {}
for i in range(len(fileList)):
    #word1 = fileList[i]
    #word2 = fileList[(i + 1) % len(fileList)]
    #key = (word1, word2)
    key = []
    for j in range(N - 1):
        key.append(fileList[(i + j) % len(fileList)])
    value = fileList[(i + j + 1) % len(fileList)]
    keyTuple = tuple(key)
    if keyTuple in d:
        d[keyTuple].append(value)
    else:
        d[keyTuple] = [value]

num_words_to_gen = input("How many words to generate: ")
## 1.2 "q" to quit, loop
##  check int convert
nWords = 0
while nWords == 0:
    try:
        num_words_to_gen = int(num_words_to_gen)
        nWords = 1
    except:
        if num_words_to_gen == "q":
            break
        else:
            num_words_to_gen = input("Please enter an integer: ")
output = []

window = choice(list(d.keys()))
for i in range(num_words_to_gen):
    word_of_choice = choice(d[window])
    output.append(word_of_choice)
    #window = (window[1], word_of_choice)
    newWindow = []
    for k in range(1 , N - 1):
        newWindow.append(window[(k)])
    newWindow.append(word_of_choice)
    window = tuple(newWindow)

## 1.3 turn into functions
## 3. Gennerate whole sentences
print("... ", end="")
for word in output:
    print(word + " ", end="")
print(" ...")