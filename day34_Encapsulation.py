#encapsulation is one of the four pillars of oop
#it means binding data and methods together inside a class
#it also helps control access to data
#encapsulation improves security and prevents accidental modification




#PUBLIC VARIABLES


#public variables can be accessed from anywhere
#inside class and outside class

class Student:

    def __init__(self):

        self.name = "Kalpana"


student = Student()

#accessing public variable outside class
print(student.name)

#output:
#Kalpana



#modifying public variable directly
student.name = "Priya"

print(student.name)

#output:
#Priya




#PROTECTED VARIABLES


#protected variables start with single underscore _
#they can still be accessed outside class
#but by convention they should not be accessed directly

class Student:

    def __init__(self):

        self._course = "MCA"


student = Student()

#possible but not recommended
print(student._course)

#output:
#MCA



#changing protected variable directly
student._course = "MBA"

print(student._course)

#output:
#MBA




#PRIVATE VARIABLES


#private variables start with double underscore __
#python performs name mangling
#direct access from outside class is restricted

class Student:

    def __init__(self):

        self.__age = 21


student = Student()

#this line will give error

# print(student.__age)

#output:
#AttributeError




#ACCESSING PRIVATE VARIABLE INSIDE CLASS


class Student:

    def __init__(self):

        self.__age = 21

    def show_age(self):

        print(self.__age)


student = Student()

student.show_age()

#output:
#21



#GETTER METHOD


#getter method is used to read private data safely

class Student:

    def __init__(self):

        self.__age = 21

    def get_age(self):

        return self.__age


student = Student()

print(student.get_age())

#output:
#21




#SETTER METHOD


#setter method is used to modify private data safely

class Student:

    def __init__(self):

        self.__age = 21

    def set_age(self, age):

        self.__age = age

    def get_age(self):

        return self.__age


student = Student()

student.set_age(25)

print(student.get_age())

#output:
#25




#REAL WORLD EXAMPLE
#BANK ACCOUNT


class BankAccount:

    def __init__(self, balance):

        #private variable
        self.__balance = balance

    def deposit(self, amount):

        #adding money to account
        self.__balance += amount

    def withdraw(self, amount):

        #checking whether sufficient balance exists
        if amount <= self.__balance:

            self.__balance -= amount

        else:

            print("insufficient balance")

    def get_balance(self):

        return self.__balance


account = BankAccount(5000)

account.deposit(1000)

account.withdraw(2000)

print(account.get_balance())

#output:
#4000




#WHY PRIVATE VARIABLES ARE USEFUL


#without encapsulation anyone can change balance

class BankAccount:

    def __init__(self):

        self.balance = 5000


account = BankAccount()

#user can directly modify balance
account.balance = 1000000

print(account.balance)

#output:
#1000000



#encapsulation prevents this type of direct access



#NAME MANGLING


#python does not completely hide private variables
#it changes their internal name

class Student:

    def __init__(self):

        self.__age = 21


student = Student()

#not recommended
#used only for understanding

print(student._Student__age)

#output:
#21




#INTERVIEW QUESTION
#PUBLIC VS PROTECTED VS PRIVATE


class Demo:

    def __init__(self):

        self.public_variable = "public"

        self._protected_variable = "protected"

        self.__private_variable = "private"


obj = Demo()

print(obj.public_variable)

#output:
#public



print(obj._protected_variable)

#output:
#protected



# print(obj.__private_variable)

#output:
#AttributeError