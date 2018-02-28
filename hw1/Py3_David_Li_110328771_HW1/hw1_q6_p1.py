f = lambda x, y: x % y == 0
def printPrimeRange(x):
    for i in range(2, (int)(x / 2)):
        if f(x, i):
            return

    print(x)

def printAllPrimeNumbers():
    for i in range(2, 101):
        printPrimeRange(i)

printAllPrimeNumbers()

# Should print 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97