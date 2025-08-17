# Get input from the user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for a fair comparison
cleaned = text.replace(" ", "").lower()

# Check if the string is the same forwards and backwards
if cleaned == cleaned[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
