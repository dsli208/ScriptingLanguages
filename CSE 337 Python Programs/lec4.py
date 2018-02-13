# Lecture 4
# '==' (value) vs. 'is' (memory location'
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print()
###################
a = "hello"
b = "hello"

print(a is b)
print()

#######################
a = "to be or not to be"
b = "to be or not to be"
print (a is b)
print()

#######################

def pal_test(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return pal_test(string[1:-1])

print(pal_test("dad"))
print(pal_test("Daddy"))
print()

##########################
print("to be or not to be".split(" "))
print()

##### DICTIONARIES ######
dct = {}
dct['name'] = "Ali"
dct['pet'] = "cat"
dct['univ'] = "Stony Brook University"
print(dct)
dct = {'name': 'ali', 'pet': 'cat'}

print()

phone_numbers = {'john': '555-555-55-55', 'mary': '444-444-44-44', 'chris': '333-333-33-33'}
print(phone_numbers)
print(phone_numbers.keys())
print(phone_numbers.values())
print('john' in phone_numbers)
print()

########## EX: COUNTING ELEMENTS ##################
def frequency(lst):
    counts = {}
    for ele in lst:
        counts[ele] = counts.get(ele,0) + 1
    return counts

print(frequency(['abc', 'def', 'abc', 'pdq', 'abc']))
print()

######### UPDATING / COPYING ###################


############ LAMBDA FUNCTIONS ############
add = lambda x, y: x + y
print(add(5, 3))
print()

############ MAP ###############
lst = [1, 2, 3, 4, 5]
print(lst)
lst2 = list(map(lambda x: x ** 2, lst))
print(lst2)
lst3 = list(filter(lambda x: x % 2 == 0, lst))
print(lst3)
list(reduce(lambda x, y: x + y, lst))
