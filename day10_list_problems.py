#list problems help improve logic building and problem solving skills


#finding minimum element in list

numbers = [10,5,20,2,15]

smallest = numbers[0]

for i in numbers:

    if i < smallest:
        smallest = i

print(smallest)

# output:
# 2



#finding second largest element

numbers = [10,45,67,23,89]

numbers.sort()

print(numbers[-2])

# output:
# 67



#removing duplicates from list

numbers = [1,2,2,3,4,4,5]

unique = []

for i in numbers:

    if i not in unique:
        unique.append(i)

print(unique)

# output:
# [1, 2, 3, 4, 5]



#linear search

numbers = [10,20,30,40,50]

key = 30

found = False

for i in numbers:

    if i == key:
        found = True
        break

print(found)

# output:
# True



#counting even and odd numbers

numbers = [1,2,3,4,5,6]

even = 0
odd = 0

for i in numbers:

    if i % 2 == 0:
        even += 1

    else:
        odd += 1

print("even =", even)
print("odd =", odd)

# output:
# even = 3
# odd = 3



#reversing a list

numbers = [1,2,3,4,5]

reverse = []

for i in numbers:
    reverse = [i] + reverse

print(reverse)

# output:
# [5, 4, 3, 2, 1]



#sum of all elements

numbers = [10,20,30,40]

total = 0

for i in numbers:
    total += i

print(total)

# output:
# 100



#finding largest and smallest together

numbers = [12,45,7,89,23]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:

    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("largest =", largest)
print("smallest =", smallest)

# output:
# largest = 89
# smallest = 7