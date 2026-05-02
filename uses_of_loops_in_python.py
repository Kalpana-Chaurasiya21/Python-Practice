#loops are used in real life problems to repeat tasks and solve problems easily
#1 counting numbers greater than 5 in a list

numbers = [2,7,4,9,1,6]
count = 0

for i in numbers:
    if i > 5:
        count = count + 1

print(count)


#2 finding maximum number in list

numbers = [10,25,3,89,45]

max = numbers[0]

for i in numbers:
    if i > max:
        max = i

print(max)


#3 reversing a string using loop

name = "kalpana"
rev = ""

for i in name:
    rev = i + rev

print(rev)


#4 checking palindrome using loop

word = "madam"
rev = ""

for i in word:
    rev = i + rev

if word == rev:
    print("palindrome")
else:
    print("not palindrome")


#5 counting vowels in a string

name = "kalpana"
count = 0

for i in name:
    if i in "aeiou":
        count = count + 1

print(count)


#6 sum of elements in list

numbers = [1,2,3,4,5]
sum = 0

for i in numbers:
    sum = sum + i

print(sum)


#7 printing pattern using loop

for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()


#8 searching element in list

numbers = [10,20,30,40]
key = 30

for i in numbers:
    if i == key:
        print("found")
        break


#9 removing duplicates from list

numbers = [1,2,2,3,4,4,5]
unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)