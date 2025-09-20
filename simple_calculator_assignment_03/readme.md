# Simple Calculator Program

**Author:** Muhammad Awais

---

## 📌 Overview

This project is a simple calculator program written in **Python**. It demonstrates the use of a single function `calculator()` to perform basic arithmetic operations such as:

* Addition (+)
* Subtraction (-)
* Multiplication (\*)
* Division (/)

The program supports both **demo examples** (predefined values) and an **interactive mode** where users can input their own numbers and operator.

---

## 🚀 Features

* Single function implementation with `return`
* Handles division by zero with an error message
* Clean and simple code structure
* Works with both integers and floats

---

## 🧩 Code Structure

### 1. Function Definition

```python
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
```

### 2. Demo Examples

```python
print(">>> Demo Examples <<<")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
```

### 3. Interactive Mode

```python
print(">>> Simple Calculator <<<")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print("Result:", result)
```

---

## 🎯 How to Run

1. Save the program as `calculator.py`
2. Run the program in your terminal or IDE:

   ```bash
   python main.py
   ```
3. First, it will show demo examples.
4. Then, you can use the interactive calculator.

---

## 📖 Example Output

```
>>> Demo Examples <<<
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 / 0 = Error: Division by zero

>>> Simple Calculator <<<
Enter first number: 20
Enter second number: 4
Enter operator (+, -, *, /): *
Result: 80.0
```

---

## 📜 Copyright

© 2025 Muhammad Awais. All rights reserved.

