#modules are files that contain functions, variables and classes
#python provides many built-in modules that can be imported and used


#importing math module

import math

print(math.sqrt(25))

# output:
# 5.0



#finding power using math module

print(math.pow(2, 3))

# output:
# 8.0



#value of pi

print(math.pi)

# output:
# 3.141592653589793



#importing random module

import random

print(random.randint(1, 10))

# output:
# random number between 1 and 10



#selecting random item from list

names = ["kalpana", "rahul", "riya"]

print(random.choice(names))

# output:
# random name from list



#importing datetime module

import datetime

today = datetime.date.today()

print(today)

# output:
# current date



#current date and time

now = datetime.datetime.now()

print(now)

# output:
# current date and time



#from import statement

from math import sqrt

print(sqrt(36))

# output:
# 6.0



#importing specific function

from random import randint

print(randint(1, 5))

# output:
# random number between 1 and 5