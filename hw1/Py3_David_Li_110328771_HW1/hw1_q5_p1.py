def passwordCheck(s):
    # define tests the password must pass to be deemed string
    lengthTestValue = lengthTest(s)
    numTestValue = False
    alphaTestValue = False
    specialTestValue = False
    noIncValTestValue = True
    distinctCharTestValue = False

    # Numeric, alphabet, and special test
    # Also tests for no previous character, more than two consecutive times
    increasingChars = 1
    previousChar = '\0'
    previousCharOccurrences = 0
    distinctChars = []
    for c in s:
        if c >= '0' and c <= '9':
            numTestValue = True
        elif (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
            alphaTestValue = True
        else:
            specialTestValue = True

        # Test for previous character equivalence to current one
        if previousChar != '\0':
            if c == previousChar:
                previousCharOccurrences += 1
                if previousCharOccurrences > 2:
                    return False
            else:
                previousCharOccurrences = 1
                previousChar = c

            if c not in distinctChars:
                distinctChars.extend(c)


            # Check for consecutive ASCII/ord value
            if ord(c) - ord(previousChar) == 1:
                increasingChars += 1
            else:
                increasingChars = 1

            # Increasing value pattern test
            if increasingChars > 3:
                noIncValTestValue = False
        else:
            previousChar = c
            distinctChars.extend(c)


    # Distinct character test
    if len(distinctChars) >= (int)(len(s) / 2):
        distinctCharTestValue = True

    return lengthTestValue and numTestValue and alphaTestValue and specialTestValue and noIncValTestValue and distinctCharTestValue





# Test length
def lengthTest(s):
    return len(s) >= 8
