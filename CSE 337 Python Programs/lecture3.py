Python 2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5 / 2
2
>>> 10 / 7
1
>>> 5 / 2.0
2.5
>>> sum = 0
>>> count = 0
>>> num = input("Enter your number: ")
Enter your number: 10
>>> while num != -1:
	sum = sum + num
	count = count + 1
	num = input("Enter your number: ")

	
Enter your number: 20
Enter your number: 14
Enter your number: 36
Enter your number: 17
Enter your number: -1
>>> print "The average is", sum / count
The average is 19
>>> # CANNOT DO INCREMENTING SYNTAX IN PYTHON
>>> 
# If we enter -1, doesn't work --> 0 DIVISION
>>> while True:
	num = input("Enter number: ")
	if num == -1:
		break

	
Enter number: 0
Enter number: 0
Enter number: -1
>>> for num in range (2, 6):
	if num % 2 == 0:
		print "Found an even number"
		continue
	print "Found a number", num

	
Found an even number
Found a number 3
Found an even number
Found a number 5
>>> def area_of_rect(w, h):
	return w * h
print 'the area of the rectangle with dimensions 2x3 is', area_of_rect(2, 3)
SyntaxError: invalid syntax
>>> def area_of_rect(w, h):
	return w * h
print 'the area of the 2x3 rectangle is', area_of_rect(2, 3)
SyntaxError: invalid syntax
>>> def area_of_rect(w, h):
	return w * h

>>> print 'the area of the 2x3 rectangle is', area_of_rect(2, 3)
the area of the 2x3 rectangle is 6
>>> import math
>>> def vol_of_radius(r):
	return 4 * math.pi * r * r * r / 3.0

>>> print vol_of_radius(5)
523.598775598
>>> def factorial(n):
	if n == 0:
		return 0
	else:
		return n * factorial(n - 1)

	
>>> print factorial(6)
0
>>> def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

	
>>> print factorial(6)
720
>>> lst = [4, 2, 1, 6, 19]
>>> lsttwo = [5, 'hello', lst]
>>> def list_sum(lst):
	if len(lst) == 0:
		return 0
	else:
		return lst[0] + list_sum(lst[1:])

	
>>> print list_sum(lsttwo)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print list_sum(lsttwo)
  File "<pyshell#61>", line 5, in list_sum
    return lst[0] + list_sum(lst[1:])
  File "<pyshell#61>", line 5, in list_sum
    return lst[0] + list_sum(lst[1:])
  File "<pyshell#61>", line 5, in list_sum
    return lst[0] + list_sum(lst[1:])
TypeError: can only concatenate list (not "int") to list
>>> print list_sum(lst)
32
>>> # list_sum only works with ints, lsttwo has strings and lists also
>>> lsttwo
[5, 'hello', [4, 2, 1, 6, 19]]
>>> lst1 = [1, 2]
>>> lst2 = [1, 2, lst1]
>>> lst2
[1, 2, [1, 2]]
>>> lst1.append(lst2)
>>> lst1
[1, 2, [1, 2, [...]]]
>>> # ^ "Black hole" because the lists refer to each other in memory"
>>> lst[:2]
[4, 2]
>>> 
