#do while loop means loop will run at least one time
#even if condition is false
#python does not have direct do while loop
#we can create it using while True


#basic example printing numbers from 1 to 5

i = 1

while True:
    print(i)
    i = i + 1
    if i > 5:
        break



#taking input at least one time

while True:
    num = int(input("enter number: "))
    print("you entered", num)
    if num == 0:
        break



#multiplication table using do while logic

num = 5
i = 1

while True:
    print(num,"x",i,"=",num*i)
    i = i + 1
    if i > 10:
        break



#menu driven example
#this will run at least one time and then ask user to continue

while True:
    print("1. say hello")
    print("2. exit")

    choice = int(input("enter choice: "))

    if choice == 1:
        print("hello")
    elif choice == 2:
        break