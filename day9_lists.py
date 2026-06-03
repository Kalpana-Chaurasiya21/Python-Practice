#lists are used to store multiple values in a single variable
#lists are written using square brackets []


#creating a list

numbers = [10,20,30,40,50]

print(numbers)

# output:
# [10, 20, 30, 40, 50]



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



#list slicing

print(numbers[1:4])

# output:
# [20, 30, 40]



#changing list element

numbers[0] = 100

print(numbers)

# output:
# [100, 20, 30, 40, 50]



#adding element using append()

numbers.append(60)

print(numbers)

# output:
# [100, 20, 30, 40, 50, 60]



#inserting element at specific position

numbers.insert(1,15)

print(numbers)

# output:
# [100, 15, 20, 30, 40, 50, 60]



#removing element using remove()

numbers.remove(30)

print(numbers)

# output:
# [100, 15, 20, 40, 50, 60]



#removing last element using pop()

numbers.pop()

print(numbers)

# output:
# [100, 15, 20, 40, 50]



#finding length of list

print(len(numbers))

# output:
# 5



#looping through list

for i in numbers:
    print(i)

# output:
# 100
# 15
# 20
# 40
# 50



#sum of list elements

total = 0

for i in numbers:
    total = total + i

print(total)

# output:
# 225



#finding maximum element

largest = numbers[0]

for i in numbers:

    if i > largest:
        largest = i

print(largest)

# output:
# 100



#checking element in list

print(20 in numbers)
print(200 in numbers)

# output:
# True
# False