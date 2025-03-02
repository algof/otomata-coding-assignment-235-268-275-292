import re

def is_valid_expression(expr):
    expr = expr.replace(" ", "")  # Menghilangkan spasi untuk memudahkan pengecekan

    print("Checking:", expr)
    
    # Mengecek apakah tanda kurung sudah seimbang
    if not is_balanced(expr):
        return False

    # Base case: if expr is just a number
    if re.fullmatch(r"\d+", expr):  # Match whole numbers
        return True

    # If the expression is enclosed in a single pair of valid parentheses, check the inside
    if expr[0] == '(' and expr[-1] == ')' and is_balanced(expr[1:-1]):
        return is_valid_expression(expr[1:-1])

    # Try to find a valid operator not inside parentheses
    index = find_main_operator(expr)
    if index == -1:
        return False

    left = expr[:index]
    right = expr[index+1:]

    # Both left and right parts must be valid expressions
    return is_valid_expression(left) and is_valid_expression(right)

def is_balanced(expr):
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def find_main_operator(expr):
    print("Finding main operator in:", expr)
    """Finds the main operator that is not inside parentheses."""
    level = 0
    for i in range(len(expr)):
        print("Level:", level, "Char:", expr[i])
        if expr[i] == '(':
            level += 1
        elif expr[i] == ')':
            level -= 1
        elif expr[i] in "+-*/" and level == 0:
            return i  # Return the position of the operator outside parentheses
    return -1  # No valid operator found

# Test cases
# print(is_valid_expression("2)-4("))        # False (invalid)
print(is_valid_expression("(3+(4-)8)"))    # False (invalid)
# print(is_valid_expression("2(/8+9)"))      # False (invalid)
# print(is_valid_expression("(3+5)+6)"))     # False (invalid)
# print(is_valid_expression("(1+9)-(4+5)"))  # True (valid)
# print(is_valid_expression("(3+(4-)8)"))    # False (invalid)
# print(is_valid_expression("(7+(2*3))"))    # True (valid)
# print(is_valid_expression("((5+)3)"))      # False (invalid)