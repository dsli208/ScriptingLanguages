def getWordDictionary(filepath):
    words = {}

    f = open(filepath, 'r',encoding="utf-8") #Update this later to suit the file name you are reading from

    for line in f.readlines():
        for word in line.split():
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1

    f.close()

    print(words)
    return words

getWordDictionary('gutenburg.txt')