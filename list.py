#lists are used to store multiple values in a single variable
#list is written using square brackets []

#creating list

numbers = [1,2,3,4,5]
print(numbers)


#accessing elements using index

print(numbers[0])
print(numbers[2])


#negative indexing

print(numbers[-1])


#looping through list

for i in numbers:
    print(i)


#length of list

print(len(numbers))


#adding elements

numbers.append(6)
print(numbers)


#inserting element at specific position

numbers.insert(1,10)
print(numbers)


#removing element

numbers.remove(3)
print(numbers)


#pop element (removes last element)

numbers.pop()
print(numbers)


#sorting list

numbers.sort()
print(numbers)


#reversing list

numbers.reverse()
print(numbers)


#checking element in list

print(2 in numbers)
print(10 not in numbers)


#sum of list elements

total = 0

for i in numbers:
    total = total + i

print(total)


#finding maximum element

max = numbers[0]

for i in numbers:
    if i > max:
        max = i

print(max)