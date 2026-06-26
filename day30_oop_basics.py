#object oriented programming (oop) is a programming paradigm
#it helps organize code using classes and objects
#oop makes code reusable manageable and scalable
#real world examples include students cars employees bank accounts etc.



#creating a class
#a class is a blueprint or template
#it defines what data and behavior an object will have

class Student:

    pass



#creating an object
#an object is an instance of a class
#multiple objects can be created from one class

student1 = Student()

print(student1)

#output:
#<__main__.Student object at memory_address>



#class attributes
#variables defined inside class
#shared by all objects of that class

class Student:

    course = "MCA"

student1 = Student()

print(student1.course)

#output:
#MCA



#constructor method
#__init__() runs automatically when object is created
#used to initialize object data

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student1 = Student("Kalpana", 21)

print(student1.name)
print(student1.age)

#output:
#Kalpana
#21



#self refers to the current object
#it allows each object to store its own data

class Student:

    def __init__(self, name):

        self.name = name

student1 = Student("Kalpana")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)

#output:
#Kalpana
#Rahul



#creating methods inside class
#methods are functions that belong to a class

class Student:

    def __init__(self, name):

        self.name = name

    def introduce(self):

        print("my name is", self.name)

student1 = Student("Kalpana")

student1.introduce()

#output:
#my name is Kalpana



#creating multiple objects

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student1 = Student("Kalpana", 21)
student2 = Student("Rahul", 22)

print(student1.name)
print(student2.name)

#output:
#Kalpana
#Rahul



#real world example
#creating a bank account class

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):

        print("current balance =", self.balance)

account1 = BankAccount("Kalpana", 5000)

account1.show_balance()

#output:
#current balance = 5000



#modifying object attributes

class Student:

    def __init__(self, name):

        self.name = name

student1 = Student("Kalpana")

print(student1.name)

student1.name = "Priya"

print(student1.name)

#output:
#Kalpana
#Priya



#checking object type

class Student:

    pass

student1 = Student()

print(type(student1))

#output:
#<class '__main__.Student'>



#important interview question

#class = blueprint
#object = real instance created from blueprint

class Car:

    pass

car1 = Car()
car2 = Car()

print(type(car1))

#output:
#<class '__main__.Car'>