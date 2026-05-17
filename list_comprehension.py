#list comprehension is used to create lists in a short and easy way
#it replaces long for loop code in one line


#basic example

numbers = [1,2,3,4,5]

square = [i*i for i in numbers]

print(square)



#creating list of even numbers

numbers = [1,2,3,4,5,6,7,8]

even = [i for i in numbers if i % 2 == 0]

print(even)



#creating list of odd numbers

odd = [i for i in numbers if i % 2 != 0]

print(odd)



#converting all strings to uppercase

names = ["kalpana","rahul","riya"]

upper_names = [i.upper() for i in names]

print(upper_names)



#using range

numbers = [i for i in range(1,11)]

print(numbers)



#list comprehension with condition

numbers = [1,2,3,4,5]

result = ["even" if i%2==0 else "odd" for i in numbers]

print(result)



#removing duplicates using list comprehension

numbers = [1,2,2,3,4,4,5]

unique = []

[unique.append(i) for i in numbers if i not in unique]

print(unique)