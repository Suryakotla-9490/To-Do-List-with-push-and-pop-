# Function to find the largest of three numbers
def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

# Taking user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calling the function to find the largest number
largest_number = find_largest(num1, num2, num3)

# Displaying the result
print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest_number)
