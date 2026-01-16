t1 = (3,43,53,43,43,54,3,43,4,43,32,43,43,56,765,5,43,76)
print("First: ", t1[0], " last ", t1[-1])

print("Length of tuple: ", len(t1))

l1 = ("Apple", "Banana","Banana", "Orange", "Date")
for i in l1:
    print(i)

a = False
for i in t1:
    if i == 53:
        a = True
        break
if a:
    print("Element exist into tuple")
else:
    print("Element not exist into tuple")

x = t1 + l1
print(x)
    
print("Count of element 43 is: ", x.count(43))

print("Index of element 43 is: ", t1.index(43))

l1 = [324,53,653,34,65,45]
t2 = tuple(l1)
print(t2)

l2 = list(t2)
l2.append("Banana")
print(t2)
t2 = tuple(l2)
print(t2)

t3 = ((32,4,32,43,54,65,54), (43,54,6,4,45,6,54,54))
print()
for i in t3:
    print(*i)
    print()