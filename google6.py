def is_valid_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():  # Opening bracket
            stack.append(char)
        elif char in bracket_map:  # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Remove matched opening bracket

    return len(stack) == 0  # True if all brackets matched

# Example usage
s = "{[()()]}"
print("Valid brackets:" if is_valid_brackets(s) else "Invalid brackets.")
