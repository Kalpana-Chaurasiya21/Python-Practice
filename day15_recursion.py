#recursion is a process where a function calls itself
#every recursive function must have a base case
#base case stops the function from running forever


#basic recursion example

def countdown(n):

    if n == 0:
        print("stop")

    else:
        print(n)
        countdown(n - 1)

countdown(5)

# output:
# 5
# 4
# 3
# 2
# 1
# stop



#factorial using recursion

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# output:
# 120



#sum of first n natural numbers

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))

# output:
# 15



#power of a number

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 3))

# output:
# 8



#fibonacci using recursion

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i))

# output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8



#reverse a string using recursion

def reverse_string(text):

    if len(text) == 0:
        return ""

    return text[-1] + reverse_string(text[:-1])

print(reverse_string("python"))

# output:
# nohtyp