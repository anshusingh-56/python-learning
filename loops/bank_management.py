balance = 5000
while True:
    print("\n------------------\nEnter\n1-Display Balance\n2-Withdraw\n3-Deposit\n4-Exit\n------------------\n")
    choice = int(input())

    if choice == 1:
        print("Total balance is ", balance)

    elif choice == 2:
        amount = int(input("Enrer amount u want to withdraw: "))

        if amount > balance:
            print("Insufficient balance !!!")
        else:
            balance -= amount
            print("Balance after withdraw is", balance)

    elif choice == 3:
        amount = int(input("Enrer amount u want to deposit: "))

        balance += amount
        print("Balance after deposit is", balance)

    elif choice == 4:
        break
