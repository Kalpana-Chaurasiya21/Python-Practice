#type casting is used to convert one data type into another

#converting int to float

a = 10

b = float(a)

print(b)        # output: 10.0
print(type(b))  # output: <class 'float'>


#converting float to int

x = 5.7

y = int(x)

print(y)        # output: 5
print(type(y))  # output: <class 'int'>


#converting int to string

num = 100

text = str(num)

print(text)        # output: "100"
print(type(text))  # output: <class 'str'>


#converting string to int

s = "50"

n = int(s)

print(n)        # output: 50
print(type(n))  # output: <class 'int'>


#converting string to float

s = "3.14"

f = float(s)

print(f)        # output: 3.14
print(type(f))  # output: <class 'float'>


#taking input and converting

num1 = input("enter number: ")

num1 = int(num1)

print(num1 + 5)