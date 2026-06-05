#tuples are used to store multiple values in a single variable
#tuples are written using round brackets ()
#tuples are immutable which means values cannot be changed


#creating a tuple

numbers = (10,20,30,40,50)

print(numbers)

# output:
# (10, 20, 30, 40, 50)



#accessing elements using index

print(numbers[0])
print(numbers[2])

# output:
# 10
# 30



#negative indexing

print(numbers[-1])

# output:
# 50



#tuple slicing

print(numbers[1:4])

# output:
# (20, 30, 40)



#looping through tuple

for i in numbers:
    print(i)

# output:
# 10
# 20
# 30
# 40
# 50



#finding length of tuple

print(len(numbers))

# output:
# 5



#tuple with different data types

data = (10, "kalpana", 85.5, True)

print(data)

# output:
# (10, 'kalpana', 85.5, True)



#count method
#counts how many times a value appears

numbers = (1,2,2,3,2,4)

print(numbers.count(2))

# output:
# 3



#index method
#returns index of first occurrence

print(numbers.index(3))

# output:
# 3



#tuple packing

student = ("kalpana", 21, "mca")

print(student)

# output:
# ('kalpana', 21, 'mca')



#tuple unpacking

name, age, course = student

print(name)
print(age)
print(course)

# output:
# kalpana
# 21
# mca



#converting tuple to list

numbers = (1,2,3)

temp = list(numbers)

temp.append(4)

numbers = tuple(temp)

print(numbers)

# output:
# (1, 2, 3, 4)