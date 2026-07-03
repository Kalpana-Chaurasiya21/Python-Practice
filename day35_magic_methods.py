#magic methods are also called dunder methods
#dunder means double underscore
#they start and end with double underscores
#python calls these methods automatically for different operations
#examples include __init__ __str__ __len__ __add__ and __eq__



#__init__()


#__init__ is called automatically when an object is created
#it is known as the constructor
#used to initialize object attributes

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student = Student("Kalpana", 21)

print(student.name)
print(student.age)

#output:
#Kalpana
#21




#__str__()


#__str__ returns a readable string representation of an object
#it is automatically called when print(object) is used
#without __str__ python prints memory address

class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Student Name : {self.name}"


student = Student("Kalpana")

print(student)

#output:
#Student Name : Kalpana




#__repr__()


#__repr__ returns the official representation of an object
#mainly used for debugging
#if __str__ is missing python uses __repr__

class Student:

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return f"Student('{self.name}')"


student = Student("Kalpana")

print(student)

#output:
#Student('Kalpana')




#__len__()


#__len__ is called when len() is used
#it should return an integer

class Book:

    def __init__(self, pages):

        self.pages = pages

    def __len__(self):

        return self.pages


book = Book(250)

print(len(book))

#output:
#250


#__add__()


#__add__ is called when + operator is used
#we can define how + should behave for our own objects

class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value


number1 = Number(10)

number2 = Number(20)

print(number1 + number2)

#output:
#30


#__eq__()


#__eq__ is called when == operator is used
#used to compare two objects

class Student:

    def __init__(self, marks):

        self.marks = marks

    def __eq__(self, other):

        return self.marks == other.marks


student1 = Student(90)

student2 = Student(90)

print(student1 == student2)

#output:
#True




#__lt__()


#__lt__ means less than
#called when < operator is used

class Product:

    def __init__(self, price):

        self.price = price

    def __lt__(self, other):

        return self.price < other.price


product1 = Product(500)

product2 = Product(800)

print(product1 < product2)

#output:
#True




#__gt__()


#__gt__ means greater than
#called when > operator is used

class Product:

    def __init__(self, price):

        self.price = price

    def __gt__(self, other):

        return self.price > other.price


product1 = Product(900)

product2 = Product(500)

print(product1 > product2)

#output:
#True




#__contains__()


#__contains__ is called when in keyword is used

class Team:

    def __init__(self):

        self.members = ["Aman", "Rahul", "Kalpana"]

    def __contains__(self, name):

        return name in self.members


team = Team()

print("Kalpana" in team)

#output:
#True




#__call__()


#__call__ allows an object to behave like a function
#object can be called using ()

class Greeting:

    def __call__(self):

        print("Hello Everyone")


greet = Greeting()

greet()

#output:
#Hello Everyone




#IMPORTANT INTERVIEW QUESTION
#WITHOUT __str__


class Student:

    pass


student = Student()

print(student)

#output:
#<__main__.Student object at memory_address>




#WITH __str__


class Student:

    def __str__(self):

        return "Student Object"


student = Student()

print(student)

#output:
#Student Object
