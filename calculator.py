def calculator():
    print("Welcome to the rishi's calculator")
    print ("select operations: " )
    print ("1.  Add " )
    print ("2.  substraction " )
    print ("3.  multiplicatin" )
    print ("4.  divide " )
    choice=input("Enter choiche (1/2/3/4): ")
    if choice not in ['1','2','3','4']:
        print ("Invalid number please choose between 4 options")
        return
    

    try:
            num1=float(input("enter the first number: "))
            num2=float(input("enter the second number: "))
    except ValueError:
            print("please enter valid numbers . ")
            return
    
    if choice=='1':
            print(f"Result : {num1} + {num2} = {num1+num2} ")
    elif choice=='2':
            print(f"Result : {num1} - {num2} = {num1-num2} ")
    elif choice=='3':
            print(f"Result : {num1} * {num2} = {num1*num2} ")
    elif choice=='4':
            if num2==0:
             print("cannot divide by zero!")
            else:
             print(f"Result : {num1} / {num2} = {num1/num2} ")
             
             
calculator()




    
