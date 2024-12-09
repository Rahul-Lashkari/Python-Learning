# Simulating a do-while loop in Python
print("Simulating a do-while loop:")

# Example: Guessing game
secret_number = 7
guess = -1  # Initialize with a value that ensures the loop runs at least once

while True:  # Simulates the "do" block
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break  # Exit the loop
    else:
        print("Wrong guess, try again!")

print("Game over!")
