def is_balanced(expression):
    stack = []
    
    pairs = {')' : '(' , ']' : '[' , '}' : '{'}
    for char in expression:
        if char in '{([' :
            stack.append(char)
        elif char in '])}' :
            if not stack:
                return False
            top = stack.pop()
            
            if pairs[char] !=top:
                return False
    return not stack
espr = input("Enter the expression : ")
if is_balanced(espr):
    print("Is Balanced")
else:
    print("Is not Balanced")            