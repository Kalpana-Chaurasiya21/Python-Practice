#generator
#a generator is a special type of iterator
#it generates values one at a time instead of storing everything in memory
#very useful when working with large amounts of data



#normal function
#returns all values at once using return

def numbers():

    return [1, 2, 3, 4, 5]

print(numbers())

#output:
#[1, 2, 3, 4, 5]



#generator function
#uses yield instead of return
#yield sends one value at a time

def numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print(numbers())

#output:
#<generator object numbers at memory_address>



#getting values from generator using next()

def numbers():

    yield 1
    yield 2
    yield 3

generator_object = numbers()

print(next(generator_object))

#output:
#1



print(next(generator_object))

#output:
#2



print(next(generator_object))

#output:
#3



#generator remembers its previous state
#it continues from where it stopped

def greetings():

    print("first line executed")
    yield "hello"

    print("second line executed")
    yield "welcome"

generator_object = greetings()

print(next(generator_object))

#output:
#first line executed
#hello



print(next(generator_object))

#output:
#second line executed
#welcome



#using generator with loop
#for loop automatically handles next()

def count_numbers():

    yield 1
    yield 2
    yield 3
    yield 4

for number in count_numbers():

    print(number)

#output:
#1
#2
#3
#4



#creating generator using loop
#values are generated one by one

def count_to_five():

    for number in range(1, 6):

        yield number

for number in count_to_five():

    print(number)

#output:
#1
#2
#3
#4
#5



#generator expression
#similar to list comprehension
#but uses round brackets instead of square brackets

numbers = (number ** 2 for number in range(1, 6))

print(numbers)

#output:
#<generator object>



for value in numbers:

    print(value)

#output:
#1
#4
#9
#16
#25



#list comprehension stores everything in memory

numbers = [number ** 2 for number in range(1, 6)]

print(numbers)

#output:
#[1, 4, 9, 16, 25]



#generator expression creates values only when needed

numbers = (number ** 2 for number in range(1, 6))

print(next(numbers))

#output:
#1



print(next(numbers))

#output:
#4



#real world example
#suppose we need numbers from 1 to 1000000
#generator is memory efficient because values are produced one by one

def large_numbers():

    for number in range(1, 1000001):

        yield number

generator_object = large_numbers()

print(next(generator_object))

#output:
#1



print(next(generator_object))

#output:
#2



print(next(generator_object))

#output:
#3



#important interview difference

#return
#ends function immediately
#returns one value

def example():

    return 10

print(example())

#output:
#10



#yield
#pauses function and remembers its state
#can return multiple values one by one

def example():

    yield 10
    yield 20

generator_object = example()

print(next(generator_object))

#output:
#10



print(next(generator_object))

#output:
#20



#checking type of generator

def numbers():

    yield 1

generator_object = numbers()

print(type(generator_object))

#output:
#<class 'generator'>