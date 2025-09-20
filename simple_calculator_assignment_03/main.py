# =========================================
#          SIMPLE CALCULATOR PROGRAM
# =========================================
# A basic calculator that performs:
# Addition (+), Subtraction (-),
# Multiplication (*), and Division (/).
# Uses a single function with three parameters.

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operator"


# -------- Demo Examples --------
print(">>> Demo Examples <<<")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print()

# -------- Interactive Mode --------
print(">>> Simple Calculator <<<")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print("Result:", result)
print("Thank you for using the calculator!")