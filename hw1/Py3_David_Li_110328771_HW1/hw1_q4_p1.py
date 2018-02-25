def getWordDictionary(filepath):
    words = {}

    f = open(filepath, 'r') #Update this later to suit the file name you are reading from

    for line in f:
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1