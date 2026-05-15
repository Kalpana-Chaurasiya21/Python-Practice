#tuples are used to store multiple values in a single variable
#tuples are written using round brackets ()
#tuples are immutable means values cannot be changed

#creating tuple

numbers = (1,2,3,4,5)
print(numbers)


#accessing elements using index

print(numbers[0])
print(numbers[2])


#negative indexing

print(numbers[-1])


#looping through tuple

for i in numbers:
    print(i)


#length of tuple

print(len(numbers))


#tuple with different data types

data = (1,"kalpana",3.5,True)
print(data)


#tuple cannot be changed
#this will give error

#numbers[0] = 10


#converting tuple to list to modify

numbers = (1,2,3)
temp = list(numbers)

temp.append(4)

numbers = tuple(temp)

print(numbers)


#tuple packing and unpacking

person = ("kalpana",21,"mca")

name,age,course = person

print(name)
print(age)
print(course)


#count method

numbers = (1,2,2,3,4,2)
print(numbers.count(2))


#index method

print(numbers.index(3))