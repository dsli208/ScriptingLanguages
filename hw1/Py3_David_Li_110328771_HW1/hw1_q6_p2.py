lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares everything
sqList = list(map(lambda x: x**2, lst))

# Filter the odd numbers out
evenSqList = list(filter(lambda x: x % 2 == 0, sqList))
print(evenSqList)