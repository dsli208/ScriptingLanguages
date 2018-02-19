def passwordCheck(s):
    # define tests the password must pass to be deemed string
    lengthTestValue = lengthTest(s)
    numTestValue = False
    alphaTestValue = False
    specialTestValue = False
    noIncValTestValue = False
    distinctCharTestValue = False

    # Numeric, alphabet, and special test
    # Also tests for no previous character
    previousChar = 0
    for c in s:
        if c >= 48 and c <= 57:
            numTestValue = True
        elif (c >= 65 and c <= 90) or (c >= 97 and c <= 122):
            alphaTestValue = True
        else:
            specialTestValue = True

        # Test for previous character equivalence to current one
        if previousChar != 0:
            if c == previousChar:
                return False
            previousChar = c



# Test length
def lengthTest(s):
    return len(s) >= 8
