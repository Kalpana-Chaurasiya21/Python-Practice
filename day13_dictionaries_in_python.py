#dictionaries are used to store data in key value pairs
#dictionaries are written using curly brackets {}


#creating a dictionary

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

print(student)

# output:
# {'name': 'kalpana', 'age': 21, 'course': 'mca'}



#accessing values using keys

print(student["name"])
print(student["age"])

# output:
# kalpana
# 21



#adding a new key value pair

student["city"] = "banda"

print(student)

# output:
# {'name': 'kalpana', 'age': 21, 'course': 'mca', 'city': 'banda'}



#updating a value

student["age"] = 22

print(student)

# output:
# {'name': 'kalpana', 'age': 22, 'course': 'mca', 'city': 'banda'}



#removing a key value pair

student.pop("course")

print(student)

# output:
# {'name': 'kalpana', 'age': 22, 'city': 'banda'}



#getting all keys

print(student.keys())

# output:
# dict_keys(['name', 'age', 'city'])



#getting all values

print(student.values())

# output:
# dict_values(['kalpana', 22, 'banda'])



#getting keys and values together

print(student.items())

# output:
# dict_items([('name', 'kalpana'), ('age', 22), ('city', 'banda')])



#looping through keys

for key in student:
    print(key)

# output:
# name
# age
# city



#looping through values

for value in student.values():
    print(value)

# output:
# kalpana
# 22
# banda



#looping through keys and values

for key, value in student.items():
    print(key, ":", value)

# output:
# name : kalpana
# age : 22
# city : banda



#checking if key exists

print("name" in student)
print("marks" in student)

# output:
# True
# False



#nested dictionary

students = {
    1: {"name": "rahul", "age": 20},
    2: {"name": "riya", "age": 21}
}

print(students)

# output:
# {1: {'name': 'rahul', 'age': 20},
#  2: {'name': 'riya', 'age': 21}}