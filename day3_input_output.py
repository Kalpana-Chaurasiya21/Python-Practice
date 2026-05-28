#input is used to take data from user
#print is used to display output on screen


#basic output

print("hello python")



#taking input from user

name = input("enter your name: ")

print(name)



#printing message with variable

print("hello", name)



#taking integer input

age = int(input("enter your age: "))

print(age)



#taking float input

marks = float(input("enter your marks: "))

print(marks)



#taking two numbers and adding them

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print("sum =", a + b)



#multiple outputs in one print statement

city = "varanasi"
course = "mca"

print(name, age, city, course)



#formatted output using f string

print(f"my name is {name} and my age is {age}")



#checking data type of input

num = input("enter number: ")

print(type(num))  
# output: <class 'str'>