#break
#used to stop the loop immediately
#once break executes the loop terminates
#commonly used when required data is found

for number in range(1, 11):

    #stop loop when number becomes 5
    if number == 5:

        break

    #this line executes until break is reached
    print(number)

#output:
#1
#2
#3
#4



#real world example
#suppose we are searching for a specific number

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    #stop searching once value is found
    if number == 30:

        print("value found")

        break

#output:
#value found



#continue
#used to skip current iteration
#loop does not stop
#it moves directly to next iteration

for number in range(1, 6):

    #skip number 3
    if number == 3:

        continue

    print(number)

#output:
#1
#2
#4
#5



#real world example
#suppose we do not want to process invalid values

numbers = [10, -5, 20, -2, 30]

for number in numbers:

    #skip negative numbers
    if number < 0:

        continue

    print(number)

#output:
#10
#20
#30



#pass
#pass does nothing
#used as a placeholder
#helps avoid syntax errors when code will be written later

for number in range(1, 4):

    if number == 2:

        pass

    print(number)

#output:
#1
#2
#3



#real world example
#creating empty function for future implementation

def future_feature():

    pass

print("function created successfully")

#output:
#function created successfully



#enumerate()
#used when both index and value are needed
#returns index and element together
#very useful while working with lists

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):

    print(index, fruit)

#output:
#0 apple
#1 banana
#2 mango



#enumerate with custom starting index
#default index starts from 0
#we can change it using start parameter

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits, start=1):

    print(index, fruit)

#output:
#1 apple
#2 banana
#3 mango



#without enumerate
#less readable approach

fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):

    print(i, fruits[i])

#output:
#0 apple
#1 banana
#2 mango



#with enumerate
#cleaner and preferred approach

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):

    print(index, fruit)

#output:
#0 apple
#1 banana
#2 mango



#important interview difference

#break
#stops the entire loop

for number in range(1, 6):

    if number == 3:

        break

    print(number)

#output:
#1
#2



#continue
#skips only current iteration

for number in range(1, 6):

    if number == 3:

        continue

    print(number)

#output:
#1
#2
#4
#5