#abstraction is one of the four pillars of object oriented programming
#it means hiding implementation details and showing only essential features
#the user knows what an object does but not how it does it
#real world examples include atm machine car and mobile phone




#WITHOUT ABSTRACTION


#here user knows every implementation detail

class Fan:

    def start(self):

        print("checking electricity")
        print("starting motor")
        print("rotating blades")

fan = Fan()

fan.start()

#output:
#checking electricity
#starting motor
#rotating blades




#ABSTRACT CLASS


#python provides ABC module
#ABC stands for Abstract Base Class

from abc import ABC, abstractmethod



#creating an abstract class
#objects of abstract class cannot be created

class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass




#CHILD CLASS IMPLEMENTS ABSTRACT METHOD


#every child class must implement start()

class Car(Vehicle):

    def start(self):

        print("car starts using key or push button")


car = Car()

car.start()

#output:
#car starts using key or push button




#ANOTHER CHILD CLASS


class Bike(Vehicle):

    def start(self):

        print("bike starts using self start button")


bike = Bike()

bike.start()

#output:
#bike starts using self start button




#WHAT HAPPENS IF CHILD DOES NOT IMPLEMENT
#ABSTRACT METHOD


class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass



class Dog(Animal):

    pass



#creating object will give error

#dog = Dog()

#output:
#TypeError




#ABSTRACT CLASS CAN HAVE NORMAL METHODS ALSO


class Employee(ABC):

    @abstractmethod
    def salary(self):

        pass

    def company_name(self):

        print("OpenAI")


class Developer(Employee):

    def salary(self):

        print("salary is 80000")


developer = Developer()

developer.company_name()

developer.salary()

#output:
#OpenAI
#salary is 80000




#REAL WORLD EXAMPLE


class Payment(ABC):

    @abstractmethod
    def pay(self):

        pass



class CreditCard(Payment):

    def pay(self):

        print("payment completed using credit card")



class UPI(Payment):

    def pay(self):

        print("payment completed using upi")



credit = CreditCard()

upi = UPI()

credit.pay()

upi.pay()

#output:
#payment completed using credit card
#payment completed using upi


#ABSTRACT CLASS CANNOT BE INSTANTIATED


class Shape(ABC):

    @abstractmethod
    def area(self):

        pass



#shape = Shape()

#output:
#TypeError




#MULTIPLE ABSTRACT METHODS


class Smartphone(ABC):

    @abstractmethod
    def call(self):

        pass

    @abstractmethod
    def message(self):

        pass



class AndroidPhone(Smartphone):

    def call(self):

        print("calling...")

    def message(self):

        print("sending message...")


phone = AndroidPhone()

phone.call()

phone.message()

#output:
#calling...
#sending message...




#INTERVIEW QUESTION
#ABSTRACTION VS ENCAPSULATION


#abstraction
#hides implementation

#encapsulation
#hides data




#CHECKING TYPE


print(isinstance(car, Vehicle))

#output:
#True