#conditional statements are used to make decisions in a program
#the code runs based on whether a condition is true or false


#simple if statement

age = 20

if age >= 18:
    print("you can vote")



#if else statement

num = 7

if num % 2 == 0:
    print("even number")
else:
    print("odd number")



#if elif else statement

marks = 75

if marks >= 90:
    print("grade A")

elif marks >= 75:
    print("grade B")

elif marks >= 60:
    print("grade C")

else:
    print("grade D")



#finding larger number

a = 20
b = 15

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")



#finding largest among three numbers

a = 10
b = 25
c = 18

if a > b and a > c:
    print(a, "is largest")

elif b > c:
    print(b, "is largest")

else:
    print(c, "is largest")



#checking positive negative or zero

num = -5

if num > 0:
    print("positive")

elif num < 0:
    print("negative")

else:
    print("zero")



#nested if statement

username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":
        print("login successful")

    else:
        print("wrong password")

else:
    print("invalid username")
