#loops are used when we want to run same code multiple times
#they save time and reduce writing same code again and again

#uses of loops in python
#1 printing numbers
#2 printing items from list
#3 taking repeated input
#4 creating patterns
#5 checking conditions multiple times



#printing numbers from 1 to 10 using for loop
#for loop is used when number of iterations is known

for i in range(1,11):
    print(i)



#printing even numbers using loop
#this loop checks numbers divisible by 2

for i in range(1,11):
    if i % 2 == 0:
        print(i)



#printing elements of list using loop
#loop goes through each element one by one

fruits = ["apple","banana","mango","grapes"]

for i in fruits:
    print(i)



#printing each character of string
#loop can also work on strings

name = "kalpana"

for i in name:
    print(i)



#sum of numbers from 1 to 5 using loop

sum = 0

for i in range(1,6):
    sum = sum + i

print(sum)



#while loop example
#while loop runs until condition becomes false

i = 1

while i <= 5:
    print(i)
    i = i + 1



#using loop for multiplication table

num = 5

for i in range(1,11):
    print(num,"x",i,"=",num*i)



#nested loop
#loop inside another loop
#used for patterns and matrix problems

for i in range(1,4):
    for j in range(1,4):
        print("*",end=" ")
    print()



#break statement
#used to stop loop immediately

for i in range(1,10):
    if i == 6:
        break
    print(i)



#continue statement
#used to skip a particular iteration

for i in range(1,6):
    if i == 3:
        continue
    print(i)