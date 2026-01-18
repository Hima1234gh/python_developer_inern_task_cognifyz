"""Write a Python program that generates a
random number between 1 and 100. The
user should then try to guess the number.
The program should provide hints such as
"too high" or "too low" until the correct
number is guessed."""


import random  # Used to generate a random number

# Define constants for the guessing range and hint sensitivity
MIN_RANGE = 1
MAX_RANGE = 100
CLOSE_DISTANCE = 5


def guess_number_game() -> None:
    """
    Generates a random number and allows the user to guess it.
    Provides hints until the correct number is guessed.
    """

    # Generate a random number within the specified range
    random_number = random.randint(MIN_RANGE, MAX_RANGE)

    # Loop until the user guesses the correct number
    while True:
        try:
            # Take user input and convert it to an integer
            guess = int(input(f"Guess a number between {MIN_RANGE} and {MAX_RANGE}: "))
        except ValueError:
            # Handle non-integer input
            print("Please enter a valid integer.")
            continue

        # Check if the guessed number is within the valid range
        if not MIN_RANGE <= guess <= MAX_RANGE:
            print(f"Please guess a number within {MIN_RANGE} and {MAX_RANGE}.")
            continue

        # Calculate the difference between guess and actual number
        difference = abs(random_number - guess)

        # Check conditions and give appropriate hints
        if difference == 0:
            print(f"Congratulations! You've guessed the correct number: {random_number}")
            break
        elif difference <= CLOSE_DISTANCE:
            print("You are very close!")
        elif guess > random_number:
            print("Too High")
        else:
            print("Too Low")


def main() -> None:
    # Entry point of the program
    guess_number_game()


# Ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
