#dictionary is used to store data in key value pair
#dictionary is written using curly brackets {}

#creating dictionary

student = {
    "name":"kalpana",
    "age":21,
    "course":"mca"
}

print(student)



#accessing values using keys

print(student["name"])
print(student["age"])



#adding new value in dictionary

student["city"] = "lucknow"

print(student)



#updating value

student["age"] = 22

print(student)



#removing element using pop()

student.pop("course")

print(student)



#looping through dictionary
#this prints keys

for i in student:
    print(i)



#printing values

for i in student.values():
    print(i)



#printing both keys and values

for key,value in student.items():
    print(key,":",value)



#checking key in dictionary

print("name" in student)
print("marks" not in student)



#length of dictionary

print(len(student))



#nested dictionary

students = {
    1:{"name":"rahul","age":20},
    2:{"name":"riya","age":21}
}

print(students)



#dictionary using input

person = {}

person["name"] = input("enter name: ")
person["age"] = int(input("enter age: "))

print(person)