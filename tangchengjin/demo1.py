
def imiwrite(filename, N_gram, num_to_gen):
    ## 1. rewrite: in functions
    from random import choice
    ## 1.1. try.. except check file exists
    flag = 0
    while flag == 0 :
        try :
            fhand = open(filename)
            print(fhand)
            flag = 1
        except :
            filename = input("Can't find the file, please enter the file name again: ")

    ## 2. N-gram instead of 3
    fileList = open(filename).read().split()
    d = {}
    for i in range(len(fileList)):
        #word1 = fileList[i]
        #word2 = fileList[(i + 1) % len(fileList)]
        #key = (word1, word2)
        key = []
        for j in range(N_gram - 1):
            key.append(fileList[(i + j) % len(fileList)])
        value = fileList[(i + j + 1) % len(fileList)]
        keyTuple = tuple(key)
        if keyTuple in d:
            d[keyTuple].append(value)
        else:
            d[keyTuple] = [value]

    ## 1.2 "q" to quit, loop
    ##  check int convert
    nWords = 0
    while nWords == 0:
        try:
            num_to_gen = int(num_to_gen)
            nWords = 1
        except:
            if num_to_gen == "q":
                break
            else:
                num_to_gen = input("Please enter an integer: ")
    output = []

    window = choice(list(d.keys()))
    for i in range(num_to_gen):
        word_of_choice = choice(d[window])
        output.append(word_of_choice)
        #window = (window[1], word_of_choice)
        newWindow = []
        for k in range(1 , N_gram - 1):
            newWindow.append(window[(k)])
        newWindow.append(word_of_choice)
        window = tuple(newWindow)

    ## 1.3 turn into functions
    ## 3. Generate whole sentences
    print("... ", end="")
    for word in output:
        print(word + " ", end="")
    print(" ...")


imiwrite('hamlet.txt', 2, 300)
