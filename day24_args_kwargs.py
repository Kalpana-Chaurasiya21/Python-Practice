#functions normally take a fixed number of arguments
#but sometimes we do not know how many values the user will pass
#for such situations python provides *args and **kwargs



#*args
#used when number of positional arguments is unknown
#stores all extra values inside a tuple
#args is just a name
#the important part is the * symbol

def add_numbers(*args):

    #printing received values
    print(args)

add_numbers(10, 20, 30)

#output:
#(10, 20, 30)



#using *args to calculate sum

def add_numbers(*args):

    #starting sum from 0
    total = 0

    #looping through all values received
    for number in args:

        total += number

    print("sum =", total)

add_numbers(10, 20, 30, 40)

#output:
#sum = 100



#passing different number of values

def add_numbers(*args):

    total = 0

    for number in args:

        total += number

    print("sum =", total)

add_numbers(5, 10)

#output:
#sum = 15

add_numbers(5, 10, 15, 20, 25)

#output:
#sum = 75



#kwargs
#used when number of keyword arguments is unknown
#stores data as a dictionary
#kwargs is just a name
#the important part is the ** symbol

def student_info(**kwargs):

    #printing dictionary received
    print(kwargs)

student_info(name="kalpana", age=21, course="mca")

#output:
#{'name': 'kalpana', 'age': 21, 'course': 'mca'}



#accessing values inside kwargs

def student_info(**kwargs):

    print(kwargs["name"])

student_info(name="kalpana", age=21)

#output:
#kalpana



#looping through kwargs

def student_info(**kwargs):

    #items() gives both key and value

    for key, value in kwargs.items():

        print(key, ":", value)

student_info(name="kalpana", age=21, city="prayagraj")

#output:
#name : kalpana
#age : 21
#city : prayagraj



#using args and kwargs together

def user_details(*args, **kwargs):

    #printing tuple received from args
    print("args =", args)

    #printing dictionary received from kwargs
    print("kwargs =", kwargs)

user_details(
    101,
    102,
    103,
    name="kalpana",
    course="mca"
)

#output:
#args = (101, 102, 103)
#kwargs = {'name': 'kalpana', 'course': 'mca'}



#real world example
#suppose a shopping website receives products dynamically
#we may not know how many products user adds to cart

def cart_total(*prices):

    total = 0

    for price in prices:

        total += price

    print("total bill =", total)

cart_total(100, 200, 300, 400)

#output:
#total bill = 1000



#important interview point

#args stores values as tuple
#kwargs stores values as dictionary

def demo(*args, **kwargs):

    print(type(args))

    print(type(kwargs))

demo(10, 20, name="kalpana")

#output:
#<class 'tuple'>
#<class 'dict'>