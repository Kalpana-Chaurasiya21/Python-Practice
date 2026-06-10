#file handling is used to read and write data in files
#it allows programs to store data permanently


#writing data to a file
#w mode creates a file if it does not exist
#it removes old data and writes new data

file = open("demo.txt", "w")

file.write("hello python")

file.close()

# output:
# data written to demo.txt



#reading data from a file

file = open("demo.txt", "r")

print(file.read())

file.close()

# output:
# hello python



#appending data to a file
#a mode adds data without removing old data

file = open("demo.txt", "a")

file.write("\nwelcome to python")

file.close()

# output:
# new line added to file



#reading file again

file = open("demo.txt", "r")

print(file.read())

file.close()

# output:
# hello python
# welcome to python



#reading file line by line

file = open("demo.txt", "r")

for line in file:
    print(line)

file.close()

# output:
# hello python
# welcome to python



#using with statement
#file closes automatically

with open("demo.txt", "r") as file:

    print(file.read())

# output:
# hello python
# welcome to python



#counting words in a file

with open("demo.txt", "r") as file:

    data = file.read()

    words = data.split()

    print(len(words))

# output:
# depends on file content



#copying content from one file to another

with open("demo.txt", "r") as source:

    data = source.read()

with open("copy.txt", "w") as destination:

    destination.write(data)

# output:
# copy.txt created with same content



#checking if a word exists in file

with open("demo.txt", "r") as file:

    data = file.read()

    if "python" in data:
        print("word found")

    else:
        print("word not found")

# output:
# word found