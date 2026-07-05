#exception handling is used to handle runtime errors
#it prevents the program from crashing
#python provides try except else finally and raise for exception handling




#WHY EXCEPTION HANDLING IS NEEDED


number1 = 10
number2 = 0

#this will give ZeroDivisionError
#print(number1 / number2)




#TRY AND EXCEPT


#code that may generate an error is written inside try block
#if an error occurs python jumps to except block

try:

    number1 = 10
    number2 = 0

    print(number1 / number2)

except:

    print("cannot divide by zero")

#output:
#cannot divide by zero




#HANDLING SPECIFIC EXCEPTION


#it is a good practice to catch specific exceptions

try:

    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:

    print("index is out of range")

#output:
#index is out of range




#MULTIPLE EXCEPT BLOCKS


#different exceptions can be handled separately

try:

    number = int("hello")

except ValueError:

    print("invalid value")

except TypeError:

    print("type error occurred")

#output:
#invalid value




#USING EXCEPTION OBJECT


#exception object stores actual error message

try:

    print(10 / 0)

except ZeroDivisionError as error:

    print(error)

#output:
#division by zero




#ELSE BLOCK


#else executes only when no exception occurs

try:

    print(20 / 5)

except ZeroDivisionError:

    print("error")

else:

    print("division successful")

#output:
#4.0
#division successful




#FINALLY BLOCK


#finally always executes
#it is commonly used to close files database connections etc

try:

    print(10 / 2)

except ZeroDivisionError:

    print("cannot divide")

finally:

    print("finally block executed")

#output:
#5.0
#finally block executed




#TRY EXCEPT ELSE FINALLY TOGETHER


try:

    number = int(input("Enter a number: "))

    print(100 / number)

except ZeroDivisionError:

    print("division by zero is not allowed")

except ValueError:

    print("please enter only numbers")

else:

    print("program executed successfully")

finally:

    print("thank you")




#RAISING EXCEPTION


#raise keyword is used to generate an exception manually

age = -5

try:

    if age < 0:

        raise ValueError("age cannot be negative")

except ValueError as error:

    print(error)

#output:
#age cannot be negative




#CUSTOM EXCEPTION


#creating our own exception class

class InvalidAgeError(Exception):

    pass


age = 15

try:

    if age < 18:

        raise InvalidAgeError("age must be at least 18")

except InvalidAgeError as error:

    print(error)

#output:
#age must be at least 18




#REAL WORLD EXAMPLE
#ATM WITHDRAWAL


balance = 5000
withdraw_amount = 7000

try:

    if withdraw_amount > balance:

        raise ValueError("insufficient balance")

    balance -= withdraw_amount

    print(balance)

except ValueError as error:

    print(error)

#output:
#insufficient balance




#REAL WORLD EXAMPLE
#LOGIN


correct_password = "python123"

entered_password = "python"

try:

    if entered_password != correct_password:

        raise ValueError("incorrect password")

    print("login successful")

except ValueError as error:

    print(error)

#output:
#incorrect password




#COMMON PYTHON EXCEPTIONS


#ZeroDivisionError
#occurs when dividing by zero

try:

    print(10 / 0)

except ZeroDivisionError:

    print("cannot divide by zero")



#ValueError
#occurs when value is invalid

try:

    number = int("hello")

except ValueError:

    print("invalid conversion")



#IndexError
#occurs when invalid list index is used

try:

    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:

    print("invalid index")



#KeyError
#occurs when dictionary key does not exist

try:

    student = {

        "name": "Kalpana"

    }

    print(student["age"])

except KeyError:

    print("key not found")



#TypeError
#occurs when operation is performed on incompatible data types

try:

    print(10 + "20")

except TypeError:

    print("invalid operation")



#FileNotFoundError
#occurs when file does not exist

try:

    file = open("python_notes.txt")

except FileNotFoundError:

    print("file not found")