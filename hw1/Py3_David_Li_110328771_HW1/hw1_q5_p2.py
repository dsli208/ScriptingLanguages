from .Py3_David_Li_110328771_HW1 import hw1_q5_p1.py

strongPassword = False
while strongPassword == False:
    password = input("Please enter a password: ")
    strongPassword = passwordCheck(password)