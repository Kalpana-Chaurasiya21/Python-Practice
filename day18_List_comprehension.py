#list comprehension is a shorter way to create lists
#it can replace simple loops and make code cleaner


#creating a list using loop

numbers = []

for i in range(1,6):
    numbers.append(i)

print(numbers)

# output:
# [1, 2, 3, 4, 5]



#creating same list using list comprehension

numbers = [i for i in range(1,6)]

print(numbers)

# output:
# [1, 2, 3, 4, 5]



#square of numbers

squares = [i*i for i in range(1,6)]

print(squares)

# output:
# [1, 4, 9, 16, 25]



#even numbers only

even_numbers = [i for i in range(1,11) if i % 2 == 0]

print(even_numbers)

# output:
# [2, 4, 6, 8, 10]



#odd numbers only

odd_numbers = [i for i in range(1,11) if i % 2 != 0]

print(odd_numbers)

# output:
# [1, 3, 5, 7, 9]



#converting names to uppercase

names = ["kalpana", "rahul", "riya"]

upper_names = [name.upper() for name in names]

print(upper_names)

# output:
# ['KALPANA', 'RAHUL', 'RIYA']



#getting length of each word

words = ["python", "java", "sql"]

lengths = [len(word) for word in words]

print(lengths)

# output:
# [6, 4, 3]



#extracting vowels from a string

text = "kalpana"

vowels = [char for char in text if char in "aeiou"]

print(vowels)

# output:
# ['a', 'a', 'a']



#creating a list of first letters

names = ["kalpana", "rahul", "riya"]

first_letters = [name[0] for name in names]

print(first_letters)

# output:
# ['k', 'r', 'r']



#using if else in list comprehension

numbers = [1,2,3,4,5]

result = ["even" if i % 2 == 0 else "odd" for i in numbers]

print(result)

# output:
# ['odd', 'even', 'odd', 'even', 'odd']