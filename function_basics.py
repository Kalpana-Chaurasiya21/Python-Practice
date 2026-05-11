#functions are used to reuse code
#instead of writing same code again and again we can use functions

#creating simple function

def hello():
    print("hello")

hello()



#function with parameters
#parameters are values passed to function

def add(a,b):
    print(a + b)

add(10,20)



#function with return value
#return sends value back

def square(num):
    return num * num

result = square(5)

print(result)



#function to check even or odd

def even_odd(num):

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(8)



#function to find maximum number

def maximum(a,b):

    if a > b:
        return a
    else:
        return b

print(maximum(10,20))



#default parameter function

def greet(name="guest"):
    print("hello",name)

greet()
greet("kalpana")



#function using loop

def table(num):

    for i in range(1,11):
        print(num,"x",i,"=",num*i)

table(5)



#recursive function
#function calling itself

def countdown(n):

    if n == 0:
        print("stop")
    else:
        print(n)
        countdown(n-1)

countdown(5)



#lambda function
#small anonymous function

square = lambda x : x*x

print(square(4))