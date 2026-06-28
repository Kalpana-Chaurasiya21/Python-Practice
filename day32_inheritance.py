#inheritance is one of the most important concepts of oop
#it allows one class to acquire properties and methods of another class
#this helps in code reusability and reduces duplication

#parent class
#also called base class or super class

#child class
#also called derived class or sub class




#1. SINGLE INHERITANCE
#one child class inherits from one parent class


class Animal:

    def eat(self):

        print("animal can eat")


class Dog(Animal):

    pass


dog = Dog()

#child object can access parent method
dog.eat()

#output:
#animal can eat

#2. MULTILEVEL INHERITANCE
#grandparent -> parent -> child


class Animal:

    def eat(self):

        print("animal can eat")


class Mammal(Animal):

    def walk(self):

        print("mammal can walk")


class Dog(Mammal):

    def bark(self):

        print("dog can bark")


dog = Dog()

#accessing method from Animal class
dog.eat()

#accessing method from Mammal class
dog.walk()

#accessing own method
dog.bark()

#output:
#animal can eat
#mammal can walk
#dog can bark




#3. MULTIPLE INHERITANCE
#one child inherits from multiple parent classes


class Father:

    def skill1(self):

        print("father knows farming")


class Mother:

    def skill2(self):

        print("mother knows cooking")


class Child(Father, Mother):

    pass


child = Child()

#accessing father class method
child.skill1()

#accessing mother class method
child.skill2()

#output:
#father knows farming
#mother knows cooking




#4. HIERARCHICAL INHERITANCE
#multiple child classes inherit from same parent


class Vehicle:

    def start(self):

        print("vehicle started")


class Car(Vehicle):

    pass


class Bike(Vehicle):

    pass


car = Car()
bike = Bike()

car.start()
bike.start()

#output:
#vehicle started
#vehicle started




#5. HYBRID INHERITANCE
#combination of multiple inheritance types


class A:

    def method_a(self):

        print("method from class A")


class B(A):

    def method_b(self):

        print("method from class B")


class C(A):

    def method_c(self):

        print("method from class C")


class D(B, C):

    def method_d(self):

        print("method from class D")


obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()

#output:
#method from class A
#method from class B
#method from class C
#method from class D




#USING CONSTRUCTOR IN INHERITANCE


class Person:

    def __init__(self, name):

        self.name = name

        print("parent constructor called")


class Student(Person):

    pass


student = Student("Kalpana")

print(student.name)

#output:
#parent constructor called
#Kalpana




#SUPER()
#used to call parent class constructor or methods


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, course):

        #calling parent constructor
        super().__init__(name)

        self.course = course


student = Student("Kalpana", "MCA")

print(student.name)
print(student.course)

#output:
#Kalpana
#MCA




#IMPORTANT INTERVIEW QUESTION
#METHOD OVERRIDING


class Animal:

    def sound(self):

        print("animal makes sound")


class Dog(Animal):

    #same method as parent class
    #child class overrides parent method

    def sound(self):

        print("dog barks")


dog = Dog()

dog.sound()

#output:
#dog barks




#CHECKING INHERITANCE RELATIONSHIP


class Animal:

    pass


class Dog(Animal):

    pass


dog = Dog()

#checks whether object belongs to class
print(isinstance(dog, Dog))

#output:
#True



#checks inheritance relationship
print(issubclass(Dog, Animal))

#output:
#True