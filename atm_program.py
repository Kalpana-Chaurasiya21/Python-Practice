#simple atm program
#user can check balance, deposit and withdraw money

balance = 1000

while True:

    print("\n1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    choice = int(input("enter your choice: "))


    if choice == 1:
        print("balance =", balance)


    elif choice == 2:
        amount = int(input("enter amount to deposit: "))
        balance = balance + amount
        print("amount deposited")


    elif choice == 3:
        amount = int(input("enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("please collect your cash")
        else:
            print("insufficient balance")


    elif choice == 4:
        print("thank you")
        break


    else:
        print("invalid choice")