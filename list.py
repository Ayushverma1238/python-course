a = [1,2,"apple", 4, 5.6]
print("First: ", a[0], " Last: ", a[-1], " Length: ", len(a))

print()

l1 = [2,3,5,7,83,45]
a = sum(l1)
print("Sum: ", a, " and average is ",float( a / len(l1)))

print()

l1 = ["Apple", "Banana","Banana", "Orange", "Date"]
l1.append("Lichi")
print(l1)
l1.insert(1,"Mango")
print(l1)
print()

l1.pop()
print(l1)
l1.remove("Banana")
print(l1)
print()

l1 = [1,1,1,1,11,1,1,23,34,2,2,1]
print("Count of 1 is: ", l1.count(1))
print()

l1 = [32,35,657,43,565,4,6,34]
x  = False
for i in l1:
    if(i == 657):
        x = True
        break
if(x):
    print("Element exist into the list")
else:
    print("Element is not into the list")

l1 = [43,543,5,3,56,87]
print("Index of element 43 is: ", l1.index(43))

print("Sorting list in assending order:")
l1.sort()
print(l1)
print("Sorting list in assending order:")
l1.sort(reverse=True)
print(l1)

l1.reverse()
print("Reverse the list is: ", l1)

s = "adsjkd"
print(s.find("d"))