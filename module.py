# import math
# # Program 1
# print("Squre root of no: ", math.sqrt(625))
# # Program 2
# print("Factorial of no 5 is: ", math.factorial(5))
# # Program 3
# print("Floor value of 4.7 is: ", math.floor(4.7))
# # Program 4
# print("Ceil value of 4.7 is: ", math.ceil(4.7))
# # Program 5
# print("5 raised to the power 3 is: ", math.pow(5, 3))
# # Program 6
# print("Absolute value of -18 is ", math.fabs(-18))
# # Program 7
# print("sin 90 is ", math.sin(math.radians(90)))
# print("cos 90 is ", math.cos(math.radians(90)))
# print("tan 90 is ", math.tan(math.radians(90)))
# # Program 8
# print("GCD of no 36 and 60 is: ", math.gcd(36, 60))
# # Program 9
# e = math.exp(3)
# print("e raised to the power 3 is: ",e)

# print("log base 10 of 1000 is ", math.log10(1000))

# print("180 degree in redian ", math.radians(180))


import random

print("Random no between 1 to 10 ", random.randint(1, 10))
print("Random no between 0 to 1 ", random.random())
list = [10,20,30,40,50]
print("Random choice from list ", list, " is ", random.choice(list))

while (True):
    n = random.randint(2, 20)
    if(n % 2 == 0):
        print("Random no between 2 to 20: ", n)
        break


