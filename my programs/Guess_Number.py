import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the guess variable
guess = 0

# Start the game loop
while guess != secret_number:
    # Get the user's guess
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the guess is too high, too low, or correct
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number: {secret_number}")
        break

# If the user runs out of guesses, print the secret number
if guess != secret_number:
    print(f"You ran out of guesses. The number was {secret_number}")