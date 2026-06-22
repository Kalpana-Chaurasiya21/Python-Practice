#lambda function
#lambda is a small anonymous function
#anonymous means function without a name
#used when function logic is short and simple
#commonly used with map() filter() and sorting operations



#normal function

def square(number):

    return number ** 2

print(square(5))

#output:
#25



#same logic using lambda function
#lambda keyword is used to create function in one line

square = lambda number: number ** 2

print(square(5))

#output:
#25



#lambda function with two arguments
#returns sum of two numbers

add = lambda a, b: a + b

print(add(10, 20))

#output:
#30



#lambda function with three arguments

multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))

#output:
#24



#map()
#used to apply a function on every element of an iterable
#returns a map object
#commonly converted into list for viewing output



numbers = [1, 2, 3, 4, 5]

#applying square operation on every element
result = map(lambda number: number ** 2, numbers)

print(list(result))

#output:
#[1, 4, 9, 16, 25]



#converting all names to uppercase

names = ["kalpana", "rahul", "aman"]

result = map(lambda name: name.upper(), names)

print(list(result))

#output:
#['KALPANA', 'RAHUL', 'AMAN']



#adding 10 to every number

numbers = [10, 20, 30]

result = map(lambda number: number + 10, numbers)

print(list(result))

#output:
#[20, 30, 40]



#filter()
#used to select elements based on a condition
#returns only those values for which condition becomes True
#returns a filter object
#commonly converted into list for viewing output



numbers = [1, 2, 3, 4, 5, 6]

#keeping only even numbers

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))

#output:
#[2, 4, 6]



#keeping only odd numbers

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda number: number % 2 != 0, numbers)

print(list(result))

#output:
#[1, 3, 5]



#keeping marks greater than or equal to 50

marks = [35, 80, 45, 90, 60]

result = filter(lambda mark: mark >= 50, marks)

print(list(result))

#output:
#[80, 90, 60]



#difference between map and filter

numbers = [1, 2, 3, 4]

#map changes every element

result = map(lambda number: number * 2, numbers)

print(list(result))

#output:
#[2, 4, 6, 8]



numbers = [1, 2, 3, 4]

#filter selects elements based on condition

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))

#output:
#[2, 4]



#real world example
#suppose we have product prices
#we want to apply 10 percent discount

prices = [100, 200, 300, 400]

discounted_prices = map(
    lambda price: price * 0.9,
    prices
)

print(list(discounted_prices))

#output:
#[90.0, 180.0, 270.0, 360.0]



#important interview point

#lambda creates a small function
#map transforms data
#filter selects data