# Importing a specific function from the math_operations module
from math_operations import add

# Taking user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the imported function
result = add(num1, num2)

# Displaying the result
print(f"The sum of {num1} and {num2} is: {result}")
