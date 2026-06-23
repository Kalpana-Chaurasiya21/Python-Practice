#iterable
#an iterable is any object that can be looped through
#examples include lists tuples strings sets and dictionaries
#for loop works because these objects are iterable

numbers = [10, 20, 30, 40]

for number in numbers:

    print(number)

#output:
#10
#20
#30
#40



#string is also iterable
#for loop accesses one character at a time

text = "python"

for character in text:

    print(character)

#output:
#p
#y
#t
#h
#o
#n



#iterator
#an iterator is an object that produces values one at a time
#it keeps track of the current position
#iterator is created using iter()

numbers = [10, 20, 30]

iterator = iter(numbers)

print(iterator)

#output:
#<list_iterator object at memory_address>



#next()
#used to get the next value from an iterator
#every time next() is called iterator moves forward

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))

#output:
#10



print(next(iterator))

#output:
#20



print(next(iterator))

#output:
#30



#what happens after last value
#iterator has no more values to return
#python raises StopIteration error

numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

#print(next(iterator))

#output:
#10
#20
#StopIteration



#for loop uses iterator internally
#python automatically creates iterator behind the scenes

numbers = [1, 2, 3]

for number in numbers:

    print(number)

#output:
#1
#2
#3



#same thing done manually

numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

#output:
#1
#2
#3



#checking whether an object is iterable

text = "python"

iterator = iter(text)

print(next(iterator))

#output:
#p



print(next(iterator))

#output:
#y



#tuple is iterable

numbers = (10, 20, 30)

for number in numbers:

    print(number)

#output:
#10
#20
#30



#dictionary is iterable
#by default loop gives keys

student = {
    "name": "kalpana",
    "age": 21
}

for key in student:

    print(key)

#output:
#name
#age



#important interview question

#iterable
#can be looped over

numbers = [1, 2, 3]



#iterator
#created from iterable using iter()
#returns one value at a time using next()

iterator = iter(numbers)



#checking types

numbers = [1, 2, 3]

iterator = iter(numbers)

print(type(numbers))

#output:
#<class 'list'>



print(type(iterator))

#output:
#<class 'list_iterator'>