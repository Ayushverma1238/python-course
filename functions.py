# def greet():
#     print("Hello world")

# greet()

# def greet_user(name):
#     print("Hello ",name)
# greet_user("Ayush")

# def addition(a, b):
#     return a +b;

# a = int(input("Enter first no: "))
# b = int(input("Enter second no: "))
# print(addition(a, b))

# def squre(a):
#     return a**2

# print("Squre of ", a, " is ", squre(a))
# print("Squre of ", b, " is ", squre(b))

# def isEven(a):
#     if(a % 2 == 0):
#         print(a," is Even")
#     else:
#         print(a," is odd")

# isEven(a)
# isEven(b)

# def Max(a, b):
#     if(a > b):
#         print(a, " is greater than ", b)
#     else:
#         print(b, " is greater than ", a)

# Max(a, b)

# def ave(l1):
#     s = sum(l1)
#     return s/len(l1)

# l1 = [23,65,65,6,65,76,76,65,54,7]
# print("Average of list is: ", ave(l1))


# def fact(n):
#     if(n == 1):
#         return 1
#     return n * fact(n-1)

# print("factorial of no is, ", fact(6))

# def isPalindrom(s):
#     a = s
#     reversed(s)
#     if(s ==a):
#         return True
#     else:
#         return False
    
# print("Is palindrom ", isPalindrom("abaaba"))

# def simpleIntrest(p,t, r = 5):
#     return (p*r*t/100)

# print("Simple interest is: ", simpleIntrest(10000,5,20))

# def keyword(name, age):
#     print(f"{name} {age}")

# keyword("Ayush", 67)

def fabonacchiNo(n):
    a = 1 
    b = 1
    if(n ==1):
        print(a)
        return
  
    print(a)
    print(b)
    
    
    for i in range(2,n):
        c = a+b
        print(c)
        a = b
        b = c

# fabonacchiNo(34)
    
def largerst(l1):
    return max(l1)

l1 = [543,65,6,65,6,654,65,65,65,65,43] 
# print("Largest element is: ", largerst(l1))

def printDictItem(dict):
    print(dict.items())

dict = {
    "NAME":"Ayush",
    "Age":45
}



# printDictItem(dict)

def printLength(s):
    print(len(s))
s = {54,65,76,5,5,7}
printLength(s)
