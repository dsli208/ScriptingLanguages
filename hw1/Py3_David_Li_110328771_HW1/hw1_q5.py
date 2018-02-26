def passwordCheck(s):
    # define tests the password must pass to be deemed string
    lengthTestValue = lengthTest(s)
    numTestValue = False
    alphaTestValue = False
    specialTestValue = False
    noIncValTestValue = False
    distinctCharTestValue = False

    # Numeric, alphabet, and special test
    # Also tests for no previous character, more than two consecutive times
    previousChar = '\0'
    previousCharOccurrences = 0
    distinctChars = []
    for c in s:
        if c >= 48 and c <= 57:
            numTestValue = True
        elif (c >= 65 and c <= 90) or (c >= 97 and c <= 122):
            alphaTestValue = True
        else:
            specialTestValue = True

        # Test for previous character equivalence to current one
        if previousChar != '\0':
            if c == previousChar:
                previousCharOccurrences += 1
                if previousCharOccurrences > 2:
                    return False
            if distinctChars.index(c) < 0:
                distinctChars += 1
            previousChar = c

    # Increasing value pattern test


    # Distinct character test
    if distinctChars >= len(s) / 2:
        distinctCharTestValue = True

    return lengthTestValue and numTestValue and alphaTestValue and specialTestValue and noIncValTestValue and distinctCharTestValue





# Test length
def lengthTest(s):
    return len(s) >= 8
