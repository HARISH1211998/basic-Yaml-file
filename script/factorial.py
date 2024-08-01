def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test the function
number = 5
print(f"Factorial of {number} is {factorial(number)}")
