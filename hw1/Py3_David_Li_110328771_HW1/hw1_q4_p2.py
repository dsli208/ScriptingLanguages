
from .Py3_David_Li_110328771_HW1 import hw1_q4_p1.py

dictionary = getWordDictionary(filepath)
sortedValues = sorted(dictionary, reverse=True)[:10]

textFile = open('top10words.txt', 'w')
for i in sortedValues:
    textFile.write(i + "\n")