# import "random" module
import random
# a is the mistery number
# a takes a random value between 0 ant 9
a = random.randint (0, 9)
# b is the guess number we input
# we give b a value out of the a value range (0 - 9)
b = 10
# c is the number of tries. We start with 0
c = 0
# we start a loop that goes on for as long a and b are not the same
while b < a or b > a:
    # we add one to tries
    c = c+1
    # we input b that is an integer
    b = int(input ("Guess  :  "))
    # a and b are compared and according to the result we take feedback
    if a == b:
        print ("Correct")
        print()
    else:
        if a > b:
            print ("toooo low")
        else:
            if a < b:
                print ("tooo high")
# print a congratulations message and the number of tries
print ("Congratulations. You did it in ", c ," tries")
# end of code


