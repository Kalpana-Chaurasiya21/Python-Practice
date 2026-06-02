#strings are used to store text data in python
#strings can be written inside single quotes or double quotes


#creating strings

name = "kalpana"

print(name)

# output:
# kalpana



#accessing characters using index
#index starts from 0

print(name[0])
print(name[1])

# output:
# k
# a



#negative indexing
#-1 represents last character

print(name[-1])

# output:
# a



#string slicing
#used to get a part of string

print(name[0:4])
print(name[2:6])

# output:
# kalp
# lpan



#looping through string

for i in name:
    print(i)

# output:
# k
# a
# l
# p
# a
# n
# a



#length of string

print(len(name))

# output:
# 7



#converting to uppercase

print(name.upper())

# output:
# KALPANA



#converting to lowercase

text = "PYTHON"

print(text.lower())

# output:
# python



#removing extra spaces

text = "  hello python  "

print(text.strip())

# output:
# hello python



#replacing characters

text = "hello"

print(text.replace("h","H"))

# output:
# Hello



#checking substring

print("kal" in name)
print("xyz" in name)

# output:
# True
# False



#reversing a string

text = "python"

reverse = ""

for i in text:
    reverse = i + reverse

print(reverse)

# output:
# nohtyp



#palindrome check

word = "madam"

if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# output:
# palindrome