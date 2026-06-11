#exception handling is used to handle errors in a program
#it prevents the program from crashing


#basic try except

try:

    a = 10
    b = 0

    print(a / b)

except:

    print("error occurred")

# output:
# error occurred



#handling specific exception

try:

    num = int(input("enter a number: "))

    print(num)

except ValueError:

    print("please enter a valid number")

# output:
# if user enters abc
# please enter a valid number



#using else block
#else runs only if no exception occurs

try:

    a = 10
    b = 2

    print(a / b)

except:

    print("error")

else:

    print("division successful")

# output:
# 5.0
# division successful



#using finally block
#finally always executes

try:

    file = open("demo.txt", "r")

except:

    print("file not found")

finally:

    print("program finished")

# output:
# program finished



#multiple exceptions

try:

    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    print(a / b)

except ValueError:

    print("invalid input")

except ZeroDivisionError:

    print("cannot divide by zero")

# output examples:
# invalid input
# cannot divide by zero



#using exception as e

try:

    a = 10
    b = 0

    print(a / b)

except Exception as e:

    print("error:", e)

# output:
# error: division by zero



#real example

try:

    marks = int(input("enter marks: "))

    if marks < 0:
        raise ValueError("marks cannot be negative")

    print("marks =", marks)

except ValueError as e:

    print(e)

# output:
# marks cannot be negative