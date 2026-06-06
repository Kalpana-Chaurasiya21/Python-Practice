#sets are used to store multiple values in a single variable
#sets do not allow duplicate values
#sets are written using curly brackets {}


#creating a set

numbers = {10,20,30,40,50}

print(numbers)

# output:
# {40, 10, 50, 20, 30}
# order may be different



#duplicates are automatically removed

numbers = {1,2,2,3,4,4,5}

print(numbers)

# output:
# {1, 2, 3, 4, 5}



#adding an element

numbers.add(6)

print(numbers)

# output:
# {1, 2, 3, 4, 5, 6}



#removing an element

numbers.remove(3)

print(numbers)

# output:
# {1, 2, 4, 5, 6}



#discard method
#does not give error if element is not present

numbers.discard(10)

print(numbers)

# output:
# {1, 2, 4, 5, 6}



#checking length of set

print(len(numbers))

# output:
# 5



#looping through set

for i in numbers:
    print(i)

# output:
# prints all elements



#checking element in set

print(2 in numbers)
print(10 in numbers)

# output:
# True
# False



#union of two sets
#combines all unique elements

a = {1,2,3}
b = {3,4,5}

print(a.union(b))

# output:
# {1, 2, 3, 4, 5}



#intersection of two sets
#common elements

print(a.intersection(b))

# output:
# {3}



#difference of two sets
#elements present in first set only

print(a.difference(b))

# output:
# {1, 2}



#removing duplicates from a list

numbers = [1,2,2,3,4,4,5]

unique = set(numbers)

print(unique)

# output:
# {1, 2, 3, 4, 5}