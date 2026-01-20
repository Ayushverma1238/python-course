# Inheritance 

class Animal:
    def speak(self):
        print("Animal make sound")
    
    def sound(self):
        print("Any generic sound")
    
class Dog(Animal):
    def bark(self):
        print("Dog bark")
    def sound(self):
        print("Bho bho")

a =Animal()
d = Dog()
d.sound()
a.sound()


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def deposite(self, amount):
        self.__balance += amount;
        print("Amount deposited successful")
    
    def get_balance(self):
        return self.__balance

acc = BankAccount("Ayush", 300)
acc.deposite(500)
print(acc.get_balance())       


class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = 0

    def acceptDetail(self):
        self.name = input("Enter your name ")
        self.roll_no = int(input("Enter your roll no "))
        self.marks = int(input("Enter your marks "))
    
    def getStudetnDetail(self):
        print(f"Student name: {self.name}, Roll no: {self.roll_no}, Marks: {self.marks}")
    
s1 = Student()
s1.acceptDetail()
s1.getStudetnDetail()

class Circle:
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        print("Area of circle is: ", 3.14 * (self.redius **2))
    
    def circumference(self):
        print("Circum Ference of Circle is: ", 3.14 * 2 * self.redius)
    
c1 = Circle(4)
c1.area()
c1.circumference()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def printDetail(self):
        print(f"Employee name is: {self.name}, age is {self.age}, with salary {self.salary}")
    
E1= Employee("Balvant", 20, 20000)
E1.printDetail()

class Vehical:
    def __init__(self):
        pass
    def start(self):
        print("Vehical start")
    
class Car(Vehical):
    def drive(self):
        print("Car is drive")
    
C1 = Car()
C1.start()
C1.drive()

class GrandFather:
    def GfShow(self):
        print("Grand Father")
class Father(GrandFather):
    def FShow(self):
        print("Father")
    
class Son(Father):
    def show(self):
        print("Son")
    
S1 = Son()
S1.show()
S1.FShow()
S1.GfShow()

class Animal:
    def sound(self):
        print("Any Random sound")

class Dog(Animal):
    def sound(self):
        print("Dog sound is Bho Bho")
    
class Cat(Animal):
    def sound(self):
        print("Cat sound is Meow")
d1 = Dog()
d1.sound()

c1 = Cat()
c1.sound()

def make_sound(animal):
    animal.sound()
        

class Dog:
    def sound(self):
        print("Bho Bho")

class Cat :
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()
make_sound(cat)
make_sound(dog)

