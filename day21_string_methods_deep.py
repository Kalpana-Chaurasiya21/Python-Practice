#strings are immutable
#this means string methods do not change the original string
#most methods return a new string


#upper()
#converts all letters into uppercase
#returns a new string with all characters in capital letters
#commonly used when case sensitive comparison is not needed

text = "python"

print(text.upper())

#output:
#PYTHON



#lower()
#converts all letters into lowercase
#returns a new string with all characters in small letters
#commonly used for case insensitive comparisons

text = "PYTHON"

print(text.lower())

#output:
#python



#title()
#converts first letter of every word into uppercase
#returns a new title cased string
#commonly used for formatting names and headings

text = "hello world"

print(text.title())

#output:
#Hello World



#capitalize()
#converts first character of string into uppercase
#remaining characters become lowercase
#commonly used for sentences

text = "hello world"

print(text.capitalize())

#output:
#Hello world



#swapcase()
#converts uppercase letters to lowercase
#and lowercase letters to uppercase

text = "PyThOn"

print(text.swapcase())

#output:
#pYtHoN



#find()
#returns index position of first occurrence
#returns -1 if value is not found
#commonly used when searching text

text = "hello python"

print(text.find("python"))

#output:
#6



#rfind()
#searches from right side
#returns last occurrence index

text = "python java python"

print(text.rfind("python"))

#output:
#12



#index()
#works like find()
#but raises ValueError if value is not found

text = "hello python"

print(text.index("python"))

#output:
#6



#count()
#counts how many times a value appears in string
#returns integer count

text = "banana"

print(text.count("a"))

#output:
#3



#startswith()
#checks whether string starts with given value
#returns True if string starts with that value
#returns False otherwise
#commonly used for prefixes and validation

text = "python programming"

print(text.startswith("python"))

#output:
#True



#endswith()
#checks whether string ends with given value
#returns True if string ends with that value
#returns False otherwise
#commonly used for checking file extensions

text = "notes.pdf"

print(text.endswith(".pdf"))

#output:
#True



#isalpha()
#checks whether string contains only alphabets
#returns True if every character is a letter
#returns False if numbers spaces or symbols are present

text = "python"

print(text.isalpha())

#output:
#True



#isdigit()
#checks whether string contains only digits
#returns True if every character is a number
#returns False otherwise
#commonly used before converting input to int

text = "12345"

print(text.isdigit())

#output:
#True



#isalnum()
#checks whether string contains only letters and numbers
#returns False if spaces or symbols are present

text = "python123"

print(text.isalnum())

#output:
#True



#islower()
#checks whether all letters are lowercase
#returns True if every alphabet is lowercase

text = "python"

print(text.islower())

#output:
#True



#isupper()
#checks whether all letters are uppercase
#returns True if every alphabet is uppercase

text = "PYTHON"

print(text.isupper())

#output:
#True



#isspace()
#checks whether string contains only spaces
#returns True if string contains spaces only

text = "   "

print(text.isspace())

#output:
#True



#istitle()
#checks whether every word starts with a capital letter
#returns True if string follows title case format

text = "Hello World"

print(text.istitle())

#output:
#True



#strip()
#removes spaces from beginning and end of string
#does not remove spaces from middle

text = "   python   "

print(text.strip())

#output:
#python



#lstrip()
#removes spaces from left side only

text = "   python"

print(text.lstrip())

#output:
#python



#rstrip()
#removes spaces from right side only

text = "python   "

print(text.rstrip())

#output:
#python



#replace()
#replaces old value with new value
#returns a new modified string

text = "i like python"

print(text.replace("python", "java"))

#output:
#i like java



#split()
#splits string into a list
#default separator is space

text = "python java sql"

print(text.split())

#output:
#['python', 'java', 'sql']



#join()
#joins list elements into a single string
#separator is written before join()

languages = ["python", "java", "sql"]

print("-".join(languages))

#output:
#python-java-sql



#center()
#places string in center within specified width

text = "python"

print(text.center(20))

#output:
#       python



#ljust()
#aligns string to left side within specified width

text = "python"

print(text.ljust(20))

#output:
#python



#rjust()
#aligns string to right side within specified width

text = "python"

print(text.rjust(20))

#output:
#              python



#zfill()
#adds zeros at beginning until desired length is reached
#commonly used in ids and formatting numbers

text = "25"

print(text.zfill(5))

#output:
#00025



#len()
#returns total number of characters in string
#len() is a built in function not a string method

text = "python"

print(len(text))

#output:
#6