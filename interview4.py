balance = 1000000
transaction = []
while True:
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<ATM MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Choice 1 : Deposit money. ")
    print("Choice 2 : withdraw money. ")
    print("Choice 3 : balance check. ")
    print("Choice 4 : Transaction history. ")
    print("Choice 5 : Exit ATM machine. ")
    choice = int(input("Enter your choice from(1/5) : "))

    
    if choice ==1:
        amount = float(input("Enter the amount :"))
        balance +=amount
        transaction.append(f"Your account has been credited with ${amount}..")
        print(f"Your account has been credited with ${amount}..")
    elif choice ==2:
        amount = float(input("Enter the amount :"))
        balance -=amount
        transaction.append(f"Your account has been debited with ${amount}..")
        print(f"Your account has been debited with ${amount}..")
    elif choice ==3:
        print(f"your balance is : {balance}")
    elif choice ==4:
        print(transaction)
    elif choice ==5:
        print("Thanks for using SBI ATM , SEE YOU SOON")    
        break
    else:
        print("Invalid choice ..........")