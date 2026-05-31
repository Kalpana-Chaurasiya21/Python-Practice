#loops are used to execute a block of code multiple times
#python provides for loop and while loop


#for loop
#used when number of iterations is known

for i in range(1,6):
    print(i)

# output:
# 1
# 2
# 3
# 4
# 5



#printing even numbers using for loop

for i in range(2,11,2):
    print(i)

# output:
# 2
# 4
# 6
# 8
# 10



#sum of numbers from 1 to 5

sum = 0

for i in range(1,6):
    sum = sum + i

print(sum)

# output: 15



#multiplication table of 5

for i in range(1,11):
    print("5 x", i, "=", 5*i)

# output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50



#while loop
#used when number of iterations is not known

i = 1

while i <= 5:
    print(i)
    i = i + 1

# output:
# 1
# 2
# 3
# 4
# 5



#counting even and odd numbers

numbers = [1,2,3,4,5,6]

even = 0
odd = 0

for i in numbers:

    if i % 2 == 0:
        even = even + 1

    else:
        odd = odd + 1

print("even =", even)
print("odd =", odd)

# output:
# even = 3
# odd = 3



#break statement
#used to stop loop immediately

for i in range(1,10):

    if i == 5:
        break

    print(i)

# output:
# 1
# 2
# 3
# 4



#continue statement
#used to skip current iteration

for i in range(1,6):

    if i == 3:
        continue

    print(i)

# output:
# 1
# 2
# 4
# 5