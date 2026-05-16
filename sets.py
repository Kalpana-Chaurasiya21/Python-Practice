#sets are used to store multiple values
#sets do not allow duplicate values
#sets are written using curly brackets {}

#creating set

numbers = {1,2,3,4,5}
print(numbers)


#duplicates are automatically removed

numbers = {1,2,2,3,4,4,5}
print(numbers)


#adding element

numbers.add(6)
print(numbers)


#removing element

numbers.remove(3)
print(numbers)


#discard (no error if element not found)

numbers.discard(10)
print(numbers)


#looping through set

for i in numbers:
    print(i)


#length of set

print(len(numbers))


#set operations

a = {1,2,3}
b = {3,4,5}

#union (combine both sets)

print(a | b)

#intersection (common elements)

print(a & b)

#difference

print(a - b)


#checking element in set

print(2 in a)
print(10 not in a)