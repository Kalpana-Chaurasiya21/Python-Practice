#append()
#used to add a single element at the end of a list
#it changes the original list directly
#returns None because it modifies the list instead of creating a new one
#commonly used when new data arrives one item at a time

#creating a sample list
numbers = [10, 20, 30]

#adding one new element at the end
numbers.append(40)

#printing updated list after append operation
print(numbers)

#output:
#[10, 20, 30, 40]



#extend()
#used to add multiple elements to a list
#it takes another iterable such as list tuple or set
#each element is added separately
#it changes the original list directly
#returns None because original list is modified
#commonly used when combining data from multiple sources

#creating a sample list
numbers = [10, 20, 30]

#adding multiple values at once
numbers.extend([40, 50, 60])

#printing updated list after extend operation
print(numbers)

#output:
#[10, 20, 30, 40, 50, 60]



#important difference between append and extend

numbers = [1, 2]

#append adds the entire list as a single element
numbers.append([3, 4])

print(numbers)

#output:
#[1, 2, [3, 4]]



numbers = [1, 2]

#extend adds each element separately
numbers.extend([3, 4])

print(numbers)

#output:
#[1, 2, 3, 4]