#scope determines where a variable can be accessed
#python mainly has local global and nonlocal scope



#local variable
#created inside a function
#can only be accessed inside that function

def greet():

    message = "hello"

    print(message)

greet()

#output:
#hello



#trying to access local variable outside function
#this will give an error

# print(message)

#output:
#NameError



#global variable
#created outside all functions
#can be accessed from anywhere in the program

name = "kalpana"

def display():

    print(name)

display()

#output:
#kalpana



#accessing global variable directly

name = "kalpana"

print(name)

#output:
#kalpana



#modifying global variable inside function
#without global keyword python creates a new local variable

count = 10

def update():

    count = 20

    print(count)

update()

print(count)

#output:
#20
#10



#using global keyword
#global allows us to modify global variable inside function

count = 10

def update():

    global count

    count = 20

    print(count)

update()

print(count)

#output:
#20
#20



#global variable can be read inside function
#without using global keyword

city = "prayagraj"

def show_city():

    print(city)

show_city()

#output:
#prayagraj



#local and global variables with same name
#local variable gets higher priority inside function

name = "global name"

def display():

    name = "local name"

    print(name)

display()

print(name)

#output:
#local name
#global name



#nonlocal keyword
#used with nested functions
#allows inner function to modify variable of outer function

def outer():

    message = "hello"

    def inner():

        nonlocal message

        message = "welcome"

    inner()

    print(message)

outer()

#output:
#welcome



#without nonlocal keyword
#inner function creates a new local variable

def outer():

    message = "hello"

    def inner():

        message = "welcome"

    inner()

    print(message)

outer()

#output:
#hello



#checking variable lookup order
#python follows LEGB rule

name = "global"

def outer():

    name = "outer"

    def inner():

        name = "inner"

        print(name)

    inner()

outer()

#output:
#inner



#LEGB stands for
#L = local
#E = enclosing
#G = global
#B = built in

#python searches variables in this order
#local -> enclosing -> global -> built in



#example of built in scope

numbers = [10, 20, 30]

print(len(numbers))

#output:
#3



#important interview question

x = 100

def demo():

    x = 200

    print(x)

demo()

print(x)

#output:
#200
#100



#another interview question

x = 100

def demo():

    global x

    x = 200

demo()

print(x)

#output:
#200