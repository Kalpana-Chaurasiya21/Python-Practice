#modules are used in real programs to perform tasks easily


#1 generating random password

import random

chars = ["a","b","c","1","2","3","@","#"]

password = ""

for i in range(5):
    password = password + random.choice(chars)

print(password)  
# output: random 5 character password



#2 rolling a dice

import random

dice = random.randint(1,6)

print(dice)  
# output: number between 1 to 6



#3 finding area of circle using math module

import math

radius = 5

area = math.pi * radius * radius

print(area)  
# output: 78.53 approx



#4 finding square root of multiple numbers

import math

numbers = [4,9,16,25]

for i in numbers:
    print(math.sqrt(i))  
# output: 2.0 3.0 4.0 5.0



#5 generating random list of numbers

import random

nums = []

for i in range(5):
    nums.append(random.randint(1,100))

print(nums)  
# output: random numbers



#6 shuffling a list

import random

data = [1,2,3,4,5]

random.shuffle(data)

print(data)  
# output: list in random order



#7 using datetime module

import datetime

today = datetime.date.today()

print(today)  
# output: current date



#8 measuring execution time

import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("time taken:", end - start)



#9 using sys module

import sys

print(sys.version)  
# output: python version



#10 using os module

import os

print(os.getcwd())  
# output: current working directory