from hw1_q4_p1 import getWordDictionary

dictionary = getWordDictionary('gutenburg.txt')

sortedValues = sorted(dictionary, key = dictionary.get, reverse=True)
print(sortedValues[:10])

textFile = open('top10words.txt', 'w')
for i in sortedValues[:10]:
    writeString = str(i) + ": " + str(dictionary[i]) + " occurrences\n"
    textFile.write(writeString)