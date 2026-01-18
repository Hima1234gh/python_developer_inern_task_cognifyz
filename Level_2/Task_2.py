# Create a number guessing game where the 
#  program generates a random number 
# between a specified range, and the user tries # to guess it. Provide feedback to the user if
# their guess is too high or too low. import random

import random  # Used to generate a random number within a range


def guess_number_game():
    # Main game loop (allows replay)
    while True:
        # Get a valid number range from the user
        while True:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))

                # Ensure start is less than end
                if start >= end:
                    print("Start must be less than end.")
                else:
                    break
            except ValueError:
                # Handles non-integer input
                print("Please enter valid integers.")

        # Generate a random number within the given range
        random_number = random.randint(start, end)
        print(f"A number has been generated between {start} and {end}.")

        # Loop until the user guesses correctly
        while True:
            try:
                guess = int(input(f"Guess a number between {start} and {end}: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            # Check if guess is outside the allowed range
            if guess < start or guess > end:
                print("Guess is out of range.")

            # Correct guess
            elif guess == random_number:
                print(f"Congratulations! You guessed it right: {random_number}")
                break

            # Very close guess (within 5)
            elif abs(random_number - guess) <= 5:
                print("You are very close!")

            # Guess is too high
            elif guess > random_number:
                print("Too High")

            # Guess is too low
            else:
                print("Too Low")

        # Ask user whether they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


def main():
    # Entry point for the game
    guess_number_game()


if __name__ == "__main__":
    main()
