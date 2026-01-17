class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
s1 = Student("Ayush", 20)
s2 = Student("Balvant", 20)

print(f"Student 1 is {s1.name} {s1.age}")
print(f"Student 2 is {s2.name} {s2.age}")

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_detail(self):
        print(f"Brand name: {self.brand} and its price is: {self.price}")
    
c1 = Car("Thar", 1000000)
c1.show_detail()

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def createObj(self):
        c1 = Employee("Balvant", 54)
        c1.showDetail()
    
    def showDetail(self):
        print(self.name, self. salary)
    
e1 = Employee("Ayush", 43555)
print(e1.name, " ", e1.salary)
e1.createObj()

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def printDetail(self):
        print(f"Mobile brand is {self.brand} and model is {self.model}")
    
m1 = Mobile("Vivo", "T2")
m2 = Mobile("Apple", "iphone")
m3 = Mobile("Vivo", "IQ")

m1.printDetail();
m2.printDetail();
m3.printDetail();

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print(f"Book name {self.title} and it\'s author is {self.author}")
    
b1 = Book("Playing it my way", "Sachin Tendulkar")
b2  = Book("Heart Lamp", "Banu mustak")
b1.display()
b2.display()

class College:
    college_name = "BBD University"
    def __init__(self, student_name):
        self.student_name = student_name
    
    def printDetail(self):
        print(f"Student name: {self.student_name} and college name is: {self.college_name}")

a1 =College("Ayush")
a1.printDetail()

class Bike:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def start(self):
        print("Bike is starting......")

    def printDetail(self):
        print(f"Bike name: {self.brand} and its color is: {self.color}")
b1 = Bike("Hero", "Black")
b1.start()
b1.printDetail()

class Laptop:
    def __init__(self, brand, RAM):
        self.brand = brand
        self.RAM  = RAM

    def printValue(self):
        print(f"Your laptop brand is {self.brand} and its RAM is {self.RAM} ")
     

l1 = Laptop("HP", "12GB")
l2 = Laptop("Lenovo", "12GB")
l1.printValue()
l2.printValue()
