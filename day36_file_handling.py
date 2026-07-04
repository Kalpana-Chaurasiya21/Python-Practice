#file handling allows python programs to read write and modify files
#it is commonly used to store data permanently
#python provides open() function to work with files

#syntax
#file_object = open("file_name", "mode")



#--------------------------------------------------
#READ MODE (r)
#--------------------------------------------------

#used to read data from a file
#raises FileNotFoundError if file does not exist

file = open("sample.txt", "r")

print(file.read())

#closing file after use
file.close()

#output:
#contents of sample.txt



#--------------------------------------------------
#WRITE MODE (w)
#--------------------------------------------------

#used to write data into a file
#if file does not exist python creates it
#if file already exists old content is deleted

file = open("sample.txt", "w")

file.write("Hello Python")

file.close()

#output:
#sample.txt now contains:
#Hello Python



#--------------------------------------------------
#APPEND MODE (a)
#--------------------------------------------------

#used to add new data at the end of file
#existing content remains unchanged

file = open("sample.txt", "a")

file.write("\nLearning File Handling")

file.close()

#output:
#Hello Python
#Learning File Handling



#--------------------------------------------------
#READING ENTIRE FILE
#--------------------------------------------------

#read() returns complete file content as a string

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

#output:
#Hello Python
#Learning File Handling



#--------------------------------------------------
#READING ONE LINE
#--------------------------------------------------

#readline() reads only one line at a time

file = open("sample.txt", "r")

print(file.readline())

file.close()

#output:
#Hello Python



#--------------------------------------------------
#READING ALL LINES
#--------------------------------------------------

#readlines() returns all lines as a list

file = open("sample.txt", "r")

print(file.readlines())

file.close()

#output:
#['Hello Python\n', 'Learning File Handling']



#--------------------------------------------------
#USING WITH STATEMENT
#--------------------------------------------------

#recommended way to work with files
#file is closed automatically
#no need to call close()

with open("sample.txt", "r") as file:

    print(file.read())

#output:
#Hello Python
#Learning File Handling



#--------------------------------------------------
#CHECKING CURRENT POSITION
#--------------------------------------------------

#tell() returns current cursor position

with open("sample.txt", "r") as file:

    print(file.tell())

#output:
#0



#--------------------------------------------------
#MOVING CURSOR
#--------------------------------------------------

#seek() changes cursor position

with open("sample.txt", "r") as file:

    file.seek(6)

    print(file.read())

#output:
#Python
#Learning File Handling



#--------------------------------------------------
#READING CHARACTER BY CHARACTER
#--------------------------------------------------

#read(number) reads specified number of characters

with open("sample.txt", "r") as file:

    print(file.read(5))

#output:
#Hello



#--------------------------------------------------
#WRITING MULTIPLE LINES
#--------------------------------------------------

lines = [
    "Python\n",
    "Java\n",
    "SQL\n"
]

with open("languages.txt", "w") as file:

    file.writelines(lines)

#output:
#languages.txt contains
#Python
#Java
#SQL



#--------------------------------------------------
#FILE EXISTS AFTER WRITING
#--------------------------------------------------

with open("notes.txt", "w") as file:

    file.write("Core Python Completed")

print("file created successfully")

#output:
#file created successfully



#--------------------------------------------------
#REAL WORLD EXAMPLE
#SAVING STUDENT DETAILS
#--------------------------------------------------

name = "Kalpana"
course = "MCA"

with open("students.txt", "a") as file:

    file.write(name + " - " + course + "\n")

print("student saved successfully")

#output:
#student saved successfully



#--------------------------------------------------
#IMPORTANT INTERVIEW QUESTION
#DIFFERENCE BETWEEN WRITE AND APPEND
#--------------------------------------------------

#write mode (w)
#removes old content
#starts writing from beginning

#append mode (a)
#keeps old content
#adds new content at end