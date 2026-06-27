#A method that belongs to a specific object (instance) of a class.
#It always takes self as its first parameter, which refers to the current object calling the method.
# Most common type of method in Python OOP
# Can read and modify the object's own data (instance variables)
# Called on an object: object.method()
# Each object gets its own copy of instance data

# Instance Method Example
# self = current object; always the first parameter

class Student:

    def __init__(self, name, age, course):
        self.name   = name    # store name in this object
        self.age    = age     # store age in this object
        self.course = course  # store course in this object

    # simple instance method — no extra parameter
    def greet(self):
        print(f"Hello! My name is {self.name}")

    # instance method with a parameter
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # instance method that modifies object data
    def update_course(self, new_course):
        self.course = new_course   # updating the instance variable
        print(f"Course updated to: {self.course}")


# creating two different objects
student1 = Student("Kalpana", 21, "MCA")
student2 = Student("Riya", 22, "BCA")

student1.greet()              # output: Hello! My name is Kalpana
student2.greet()              # output: Hello! My name is Riya

student1.study("Python")     # output: Kalpana is studying Python
student2.study("Java")       # output: Riya is studying Java

student1.update_course("MBA") # output: Course updated to: MBA