#patterns are used to improve logic building
#patterns help us understand nested loops better


#1 square pattern

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

# output:
# * * * *
# * * * *
# * * * *
# * * * *



#2 right triangle pattern

for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()

# output:
# *
# * *
# * * *
# * * * *



#3 inverted triangle pattern

for i in range(4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# output:
# * * * *
# * * *
# * *
# *



#4 number pattern

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4



#5 same number pattern

for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

# output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4



#6 pyramid pattern

for i in range(1,5):

    for j in range(4-i):
        print(" ", end="")

    for k in range(i):
        print("*", end=" ")

    print()

# output:
#    *
#   * *
#  * * *
# * * * *



#7 Floyd's triangle

num = 1

for i in range(1,5):

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()

# output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10