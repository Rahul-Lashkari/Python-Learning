# Raising Custom Errors in Python
# This Python file demonstrates how to create and raise custom exceptions.

# Defining a custom exception class
class CustomError(Exception):
    pass

# Example usage of raising a custom error
def check_positive(number):
    if number < 0:
        raise CustomError("Number must be positive!")
    return f"{number} is positive."

# Testing the custom exception
try:
    result = check_positive(-5)
    print(result)
except CustomError as e:
    print(f"Caught an error: {e}")
