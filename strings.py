#strings are used to store text data in python
#string is written inside single or double quotes

#creating string
name = "kalpana"
print(name)
#accessing characters using index
#index starts from 0

print(name[0])
print(name[1])


#negative indexing
#-1 means last character
print(name[-1])


#string slicing
#used to get part of string

print(name[0:4])
print(name[2:6])


#looping through string
#we can access each character using loop
for i in name:
    print(i)


#length of string
#len() gives total number of characters

print(len(name))


#string methods

#convert to uppercase
print(name.upper())
#convert to lowercase
print(name.lower())

#remove spaces
text = "  hello  "
print(text.strip())


#checking substring

print("kal" in name)
print("xyz" not in name)


#concatenation
#joining two strings

first = "hello"
second = "world"

print(first + " " + second)


#reversing string using loop

rev = ""

for i in name:
    rev = i + rev

print(rev)


#checking palindrome

word = "madam"
rev = ""

for i in word:
    rev = i + rev

if word == rev:
    print("palindrome")
else:
    print("not palindrome")