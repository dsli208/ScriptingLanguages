def calcPearsonCoefficient(xList, yList): # where x and y are both in list form
    # defining sigma values
    xy = sumXY(xList,yList)
    sigmax = sum(xList)
    sigmay = sum(yList)

    # Now, given your sigma values, calculate the top half of r
    topHalf = xy - ((sigmax * sigmay)/len(xList))

    # Calculate the bottom half
    bottomHalfSquared = calcBottom(xList) * calcBottom(yList)
    bottomHalf = bottomHalfSquared**(0.5)

    # Finally, determine r
    r = topHalf / bottomHalf

    return r

# Function to assist in calculating the bottom
def calcBottom(xList):
    squareX = squareList(xList)
    sigmaX = sum(xList)
    return squareX - ((sigmaX**2) / len(xList))

# Several functions below to calculate all "SIGMA"/sum values
def sumXY(xList, yList):
    total = 0
    for x in xList and y in yList:
        total += (x * y)
    return total

def sum(xList):
    total = 0
    for x in xList:
        total += x
    return total

def squareList(xList):
    total = 0
    for x in xList:
        total += x**2
    return total

