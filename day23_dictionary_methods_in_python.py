#dictionary is used to store data in key value pairs
#keys must be unique
#values can be duplicated
#dictionary is mutable which means data can be modified


#get()
#used to get value using key
#returns value if key exists
#returns None if key does not exist
#safer than using square brackets because it avoids errors

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

#getting value using key
print(student.get("name"))

#output:
#kalpana



#getting a key that does not exist
print(student.get("city"))

#output:
#None



#keys()
#returns all keys present in dictionary
#result is returned as a view object

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

#printing all keys
print(student.keys())

#output:
#dict_keys(['name', 'age', 'course'])



#values()
#returns all values present in dictionary

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

#printing all values
print(student.values())

#output:
#dict_values(['kalpana', 21, 'mca'])



#items()
#returns both keys and values together
#each key value pair is returned as a tuple

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

#printing all key value pairs
print(student.items())

#output:
#dict_items([('name', 'kalpana'), ('age', 21), ('course', 'mca')])



#update()
#used to add new data or update existing data
#if key exists value gets updated
#if key does not exist new key is created

student = {
    "name": "kalpana",
    "age": 21
}

#adding a new key value pair
student.update({"city": "banda"})

print(student)

#output:
#{'name': 'kalpana', 'age': 21, 'city': 'banda'}



#updating existing value
student.update({"age": 22})

print(student)

#output:
#{'name': 'kalpana', 'age': 22, 'city': 'banda'}



#pop()
#removes key value pair using key
#returns removed value
#gives error if key is not found

student = {
    "name": "kalpana",
    "age": 21
}

#removing age key
removed_value = student.pop("age")

print(removed_value)

print(student)

#output:
#21
#{'name': 'kalpana'}



#popitem()
#removes last inserted key value pair
#returns removed key value pair as tuple

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

removed_item = student.popitem()

print(removed_item)

print(student)

#output:
#('course', 'mca')
#{'name': 'kalpana', 'age': 21}



#clear()
#removes all key value pairs from dictionary
#dictionary becomes empty

student = {
    "name": "kalpana",
    "age": 21
}

student.clear()

print(student)

#output:
#{}



#copy()
#creates a copy of dictionary
#changes in copied dictionary do not affect original dictionary

student = {
    "name": "kalpana",
    "age": 21
}

new_student = student.copy()

print(new_student)

#output:
#{'name': 'kalpana', 'age': 21}



#checking whether key exists
#in keyword returns True or False

student = {
    "name": "kalpana",
    "age": 21
}

print("name" in student)

#output:
#True



print("city" in student)

#output:
#False



#looping through keys

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

for key in student:

    print(key)

#output:
#name
#age
#course



#looping through values

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

for value in student.values():

    print(value)

#output:
#kalpana
#21
#mca



#looping through both keys and values

student = {
    "name": "kalpana",
    "age": 21,
    "course": "mca"
}

for key, value in student.items():

    print(key, ":", value)

#output:
#name : kalpana
#age : 21
#course : mca