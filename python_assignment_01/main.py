
print("\n------------------------------------")
print("\n --- Q1: Variables & Data Types --- ")
print("\n------------------------------------\n")

# Step 01: Initialize variable's:
name: str = "Muhammad Awais"
age: int = 24
is_student: bool = True

# Step 02: Converting boolean into human-readable text:
student_status: str = "Yes" if is_student else "No"

# Step 03: Final Output:
print(f"Hi, I am {name}, I am {age} years old and I am a student in PIAIC: {student_status}")

# Step 04: Checking data types:
print("\n--- Data Types ---")
print("Name Data Type        :", type(name))
print("Age Data Type         :", type(age))
print("is_student Data Type  :", type(is_student))



print("\n------------------------------------")
print("\n ---- Q2: Arithmetic Operators ---- ")
print("\n------------------------------------\n")

# Step 01: Initialize variable's:
x: int = 20
y: int = 6

# Step 02: Final Output:
print(f"Addition        :  x({x}) + y({y}) = {x + y}")
print(f"Substraction    :  x({x}) - y({y}) = {x - y}")
print(f"Multiplication  :  x({x}) * y({y}) = {x * y}")
print(f"Division        :  x({x}) / y({y}) = {x / y}")
print(f"Floor Division  :  x({x}) // y({y}) = {x // y}")
print(f"Modulus         :  x({x}) % y({y}) = {x % y}")
print(f"Exponent        :  x({x}) ** y({y}) = {x ** y}")



print("\n------------------------------------")
print("\n ---- Q3: Assignment Operators ---- ")
print("\n------------------------------------\n")

# Step 01: Initialize variable:
num: int = 10

# Step 02: Add 5 to num using += operator:
num += 5
print(f"Value after addition of 10 + 5 is              :  {num}")

# Step 03: Multiply 2 from num using *= operator:
num *= 2
print(f"Value after multiplication of 15 * 2 is        :  {num}")

# Step 04: Subtract 4 from num using -= operator:
num -= 4

# Step 04: Final Output
print(f"Final value of all operators after 30 - 4 is   :  {num}")



print("\n------------------------------------")
print("\n ---- Q4: Comparison Operators ---- ")
print("\n------------------------------------\n")


# Step 01: Initialize variables
a: int = 15
b: int = 12

# Step 02: Final Output
print(f"a({a}) > b({b})  : {a > b}")
print(f"a({a}) < b({b})  : {a < b}")
print(f"a({a}) == b({b}) : {a == b}")
print(f"a({a}) != b({b}) : {a != b}")
print(f"a({a}) >= b({b}) : {a >= b}")
print(f"a({a}) <= b({b}) : {a <= b}")


print("\n------------------------------------")
print("\n -----  Q5: Logical Operators  ---- ")
print("\n------------------------------------\n")

# Step 01: Initialize variable's
p: bool = True
q: bool = False

# Step 02: Final Output's
print(f"p({p}) AND q({q})  :  {p and q}")
print(f"p({p}) OR q({q})   :  {p or q}")
print(f"NOT p({p})         :  {not p}")
print(f"NOT q({q})         :  {not q}")



print("\n------------------------------------")
print("\n -----  Q6: Real-Life Example  ---- ")
print("\n------------------------------------\n")

# Step 01: Initialize variables
price_per_notebook: int = 80
quantity: int = 7
money_available: int = 600

# Step 02: Calculate total price
total_price: int = price_per_notebook * quantity

# Step 03: Check if money is enough
is_enough: bool = money_available >= total_price

# Step 04: Final Output
print(f"Price of one notebook: {price_per_notebook} rupees")
print(f"Total notebooks: {quantity}")
print(f"Total price: {total_price} rupees")
print(f"Money available: {money_available} rupees")
print(f"Can you buy them? {'Yes' if is_enough else 'No'}")
print(f"Remaining amount is : {money_available % total_price}")



print("\n------------------------------------")
print("\n -----  Q7: Logical Operators  ---- ")
print("\n------------------------------------\n")

# Q9: Sum and Compare Two Numbers

# Step 01: Taking user inputs
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# Step 02: Calculating the sum
total: int = first_number + second_number

# Step 03: Final Output - Sum
print(f"The sum of {first_number} and {second_number} is: {total}")

# Step 04: Compare and print the result
if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
elif first_number < second_number:
    print(f"{first_number} is less than {second_number}")
else:
    print(f"{first_number} is equal to {second_number}")