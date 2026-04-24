#Operators are symbols that tell Python to perform operartions on variables and values.
#types of operators 
#1 Arithmetic operators
#Arithmetic operators are used to perform basic arithmetic operations

# + operator used for addition of two numbers
a = 10
b = 5
print(a + b)

# - operator used to subtract one number from another
print(a - b)

# * operator used to multiply two numbers
print(a * b)

# / operator used to divide two numbers and gives decimal result
print(a / b)

# // operator used for floor division, gives only whole number
print(a // b)

# % operator used to get remainder after division
print(a % b)

# ** operator used to find power of a number
print(a ** b)


#2 Assignment operators
#Assignment operators are used to assign values to variables

# = operator assigns value to variable
x = 10
print(x)

# += operator adds value and assigns back
x += 5
print(x)

# -= operator subtracts value and assigns back
x -= 2
print(x)

# *= operator multiplies and assigns back
x *= 3
print(x)

# /= operator divides and assigns back
x /= 2
print(x)

# //= operator floor divides and assigns back
x = 20
x //= 3
print(x)

# %= operator gives remainder and assigns back
x %= 4
print(x)


#3 Comparison operators
#Comparison operators are used to compare two values and give true or false

a = 10
b = 20

# == operator (checks if both are equal)
print(a == b)

# != operator (checks if not equal)
print(a != b)

# > operator (checks greater value)
print(a > b)

# < operator (checks smaller value)
print(a < b)

# >= operator (checks greater or equal)
print(a >= b)

# <= operator (checks smaller or equal)
print(a <= b)


#4 Logical operators
#Logical operators are used to combine conditions

a = True
b = False

# and operator (true if both are true)
print(a and b)

# or operator (true if at least one is true)
print(a or b)

# not operator (reverses the result)
print(not a)


#5 Bitwise operators
#Bitwise operators work on binary numbers

a = 5
b = 3

# & operator (and operation in binary)
print(a & b)

# | operator (or operation in binary)
print(a | b)

# ^ operator (xor operation)
print(a ^ b)

# ~ operator (not operation)
print(~a)

# << operator (left shift)
print(a << 1)

# >> operator (right shift)
print(a >> 1)


#6 Membership operators
#Membership operators check if value is present in sequence

list1 = [1,2,3,4,5]

# in operator (checks if value is present)
print(3 in list1)

# not in operator (checks if value is not present)
print(10 not in list1)


#7 Identity operators
#Identity operators check if two variables refer to same object

a = [1,2,3]
b = [1,2,3]
c = a

# is operator (checks if both are same object)
print(a is c)

# is not operator (checks if both are different objects)
print(a is not b)
a=10