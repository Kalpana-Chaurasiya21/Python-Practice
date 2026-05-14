#exception handling is used to handle errors in program
#it prevents program from crashing


#basic example

try:
    a = 10
    b = 0
    print(a / b)

except:
    print("error occurred")



#handling specific exception

try:
    num = int(input("enter number: "))
    print(num)

except ValueError:
    print("invalid input")



#using else block
#else runs if no error occurs

try:
    a = 10
    b = 2
    print(a / b)

except:
    print("error")

else:
    print("division successful")



#using finally block
#finally always runs

try:
    file = open("demo.txt","r")
    print(file.read())

except:
    print("file not found")

finally:
    print("this will always execute")



#multiple exceptions

try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a / b)

except ValueError:
    print("invalid input")

except ZeroDivisionError:
    print("cannot divide by zero")



#using exception as e

try:
    a = 10
    b = 0
    print(a / b)

except Exception as e:
    print("error is:", e)