# Quick Quiz: Fibonacci Sequence

def fibonacci(n):
    """Function to print the Fibonacci sequence up to the nth term."""
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the first two terms
    a, b = 0, 1

    # Print the sequence
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update the terms
    print()


# Input: Number of terms
num = int(input("Enter the number of terms: "))
fibonacci(num)