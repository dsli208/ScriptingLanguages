from hw1_q5_p1 import passwordCheck

strongPassword = False
while strongPassword == False:
    password = input("Please enter a password: ")
    strongPassword = passwordCheck(password)
    if strongPassword == False:
        print("Not a strong enough password.  Please try again.")