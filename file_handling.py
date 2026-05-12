#file handling is used to read and write data in files

#opening file in read mode
#r means read mode

#file = open("demo.txt","r")
#print(file.read())
#file.close()



#writing data into file
#w means write mode
#it removes old data and writes new data

file = open("demo.txt","w")

file.write("hello python")

file.close()



#reading file data

file = open("demo.txt","r")

print(file.read())

file.close()



#append mode
#a means adding new data without removing old data

file = open("demo.txt","a")

file.write("\nwelcome")

file.close()



#reading file line by line

file = open("demo.txt","r")

for i in file:
    print(i)

file.close()



#using with statement
#file closes automatically

with open("demo.txt","r") as file:
    print(file.read())



#counting number of words in file

with open("demo.txt","r") as file:

    data = file.read()

    words = data.split()

    print(len(words))



#copying data from one file to another

with open("demo.txt","r") as file1:

    data = file1.read()

with open("copy.txt","w") as file2:

    file2.write(data)



#checking if word exists in file

with open("demo.txt","r") as file:

    data = file.read()

    if "python" in data:
        print("word found")
    else:
        print("word not found")