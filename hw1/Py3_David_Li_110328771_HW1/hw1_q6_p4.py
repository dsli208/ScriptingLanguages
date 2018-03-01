def count_pattern(str, pattern, replace_str):
    assert len(str) >= len(pattern)
    pattern_relationship = get_ord_relationship(pattern)
    begin = 0
    end = len(pattern)
    while end <= len(str):
        strPortion = str[begin:end]
        strPortionOrd = get_ord_relationship(strPortion)

        if strPortionOrd == pattern_relationship:
            firstPortion = str[:begin]

            endPortion = str[end:]

            str = firstPortion + replace_str

            str = str + endPortion

        begin += 1
        end += 1

    return str

def get_ord_relationship(pattern):
    ord_relationship = []
    previousChar = '\0'
    for c in pattern:
        if previousChar != '\0':
            ord_relationship.append(ord(c) - ord(previousChar))
        previousChar = c
    return ord_relationship

def replaceStrPortion(str, replace_str, begin):
    s = list(str)
    index = begin
    for c in replace_str:
        s[index] = c
        index += 1

    str = "".join(s)

print(count_pattern('David','av', '123'))