def getWordDictionary(filepath):
    words = {}

    f = open(filepath, 'r') #Update this later to suit the file name you are reading from

    for line in f:
        for word in line.split():
            if word in words:
                words[word] = words.get(word, 0) + 1
            #else:
                #words[word] = 1

    f.close()

    print(words)
    return words

getWordDictionary('gutenburg.txt')