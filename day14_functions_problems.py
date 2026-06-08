#functions are used to reuse code
#instead of writing same code again and again, we can put it inside a function


#creating a simple function

def greet():
    print("hello python")

greet()

# output:
# hello python



#function with parameters

def greet_user(name):
    print("hello", name)

greet_user("kalpana")

# output:
# hello kalpana



#function with multiple parameters

def add(a, b):
    print(a + b)

add(10, 20)

# output:
# 30



#function with return statement
#return sends a value back

def square(num):
    return num * num

result = square(5)

print(result)

# output:
# 25



#function to check even or odd

def check_even_odd(num):

    if num % 2 == 0:
        print("even")

    else:
        print("odd")

check_even_odd(8)

# output:
# even



#function to find maximum number

def maximum(a, b):

    if a > b:
        return a

    else:
        return b

print(maximum(10, 25))

# output:
# 25



#default parameter
#if no value is passed, default value is used

def greet(name="guest"):
    print("welcome", name)

greet()
greet("kalpana")

# output:
# welcome guest
# welcome kalpana



#function using loop

def table(num):

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

table(5)

# output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50



#lambda function
#small one-line function

square = lambda x: x * x

print(square(4))

# output:
# 16