#operators are symbols used to perform operations on variables and values


#arithmetic operators

a = 10
b = 3

print(a + b)   # output: 13
print(a - b)   # output: 7
print(a * b)   # output: 30
print(a / b)   # output: 3.333
print(a // b)  # output: 3
print(a % b)   # output: 1
print(a ** b)  # output: 1000



#comparison operators
#returns true or false

print(a > b)    # output: True
print(a < b)    # output: False
print(a == b)   # output: False
print(a != b)   # output: True
print(a >= b)   # output: True
print(a <= b)   # output: False



#assignment operators

x = 5

x += 2
print(x)   # output: 7

x -= 1
print(x)   # output: 6

x *= 2
print(x)   # output: 12



#logical operators

a = True
b = False

print(a and b)   # output: False
print(a or b)    # output: True
print(not a)     # output: False



#membership operators

numbers = [1,2,3,4,5]

print(3 in numbers)       # output: True
print(10 not in numbers)  # output: True



#identity operators

x = [1,2]
y = [1,2]
z = x

print(x is z)       # output: True
print(x is y)       # output: False
print(x is not y)   # output: True