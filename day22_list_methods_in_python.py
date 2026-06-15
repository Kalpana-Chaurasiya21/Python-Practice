#lists are mutable
#which means elements can be added removed or modified
#list methods are used to perform operations on lists


#append()
#adds a single element at the end of the list
#modifies the original list

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

#output:
#[10, 20, 30, 40]



#extend()
#adds multiple elements from another iterable
#each element is added separately

numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)

#output:
#[10, 20, 30, 40, 50]



#insert()
#inserts element at a specific position
#first argument is index
#second argument is value

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

#output:
#[10, 15, 20, 30]



#remove()
#removes first occurrence of given value
#gives error if value is not found

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

#output:
#[10, 30, 20]



#pop()
#removes element using index
#returns removed value
#last element is removed by default

numbers = [10, 20, 30]

removed = numbers.pop()

print(removed)
print(numbers)

#output:
#30
#[10, 20]



#index()
#returns index position of first occurrence
#gives error if value is not found

numbers = [10, 20, 30]

print(numbers.index(20))

#output:
#1



#count()
#counts how many times a value appears

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))

#output:
#3



#sort()
#sorts list in ascending order
#changes original list

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

#output:
#[10, 20, 30, 40]



#sort(reverse=True)
#sorts list in descending order

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

#output:
#[40, 30, 20, 10]



#reverse()
#reverses current order of elements

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

#output:
#[40, 30, 20, 10]



#copy()
#creates a shallow copy of list
#changes in copied list do not affect original list

numbers = [10, 20, 30]

new_list = numbers.copy()

print(new_list)

#output:
#[10, 20, 30]



#clear()
#removes all elements from list

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

#output:
#[]



#len()
#returns total number of elements in list
#len() is a built in function not a list method

numbers = [10, 20, 30, 40]

print(len(numbers))

#output:
#4



#max()
#returns largest value from list

numbers = [10, 20, 30, 40]

print(max(numbers))

#output:
#40



#min()
#returns smallest value from list

numbers = [10, 20, 30, 40]

print(min(numbers))

#output:
#10



#sum()
#returns sum of all numeric values

numbers = [10, 20, 30, 40]

print(sum(numbers))

#output:
#100