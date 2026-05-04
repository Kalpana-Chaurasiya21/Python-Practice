#patterns are used to understand loops better
#mostly used in practice to improve logic building


#1 square pattern

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


#2 right angle triangle pattern

for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()


#3 inverted right triangle

for i in range(4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()


#4 number pattern

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


#5 same number pattern

for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()


#6 pyramid pattern

for i in range(1,5):
    for j in range(4-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()


#7 inverted pyramid

for i in range(4,0,-1):
    for j in range(4-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()


#8 hollow square

for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#9 Floyd’s triangle

num = 1

for i in range(1,5):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()