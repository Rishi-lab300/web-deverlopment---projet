# Fixed exchange rate (example: 1 USD = 83.2 INR)
USD_TO_INR = 86.2
INR_TO_USD = 1 / USD_TO_INR

def convert_currency():
    print("Currency Converter:")
    print("1. Dollar to Indian Rupees")
    print("2. Indian Rupees to Dollar")
    
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        dollars = float(input("Enter amount in Dollars: "))
        rupees = dollars * USD_TO_INR
        print(f"{dollars} USD = {rupees:.2f} INR")

    elif choice == '2':
        rupees = float(input("Enter amount in Rupees: "))
        dollars = rupees * INR_TO_USD
        print(f"{rupees} INR = {dollars:.2f} USD")

    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the converter
convert_currency()
