## 1. rewrite: in functions
from random import choice
name = input("Input file name: ")  ## optional: loop
## 1.1. try.. except check file exists

## N = input("How may grams: ")
## N = 3
## 2. N-gram instead of 3
fileList = open(name).read().split()
## newline ?
d = {}
for i in range(len(fileList)):
    ## 2.1 windows length = N - 1
    word1 = fileList[i]
    word2 = fileList[(i + 1) % len(fileList)]
    key = (word1, word2)
    value = fileList[(i + 2) % len(fileList)]
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

num_words_to_gen = int(input("How many words to generate: "))
## 1.2 "q" to quit, loop
##  check int convert
output = []
window = choice(list(d.keys()))
for i in range(num_words_to_gen):
    word_of_choice = choice(d[window])
    output.append(word_of_choice)
    window = (window[1], word_of_choice)

## 1.3 turn into functions
## 3. Gennerate whole sentences
print("... ", end="")
for word in output:
    print(word + " ", end="")
print(" ...")
