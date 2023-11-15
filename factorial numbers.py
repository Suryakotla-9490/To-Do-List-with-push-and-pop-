def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

# Take user input for the number
num = int(input("Enter a number to find its factorial: "))

# Call the recursive function to find factorial
result = factorial_recursive(num)

# Display the result
print(f"The factorial of {num} is: {result}")