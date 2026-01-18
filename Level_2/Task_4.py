"""Write a Python function that generates the
Fibonacci sequence up to a given number of
terms. The function should take an integer
input from the user and display the
Fibonacci sequence up to that number of
terms."""


START = 0
NEXT = 1


def fibonacci_series(n_terms: int) -> None:
    """
    Generates and displays the Fibonacci sequence
    up to the given number of terms.
    """

    # Initialize the first two Fibonacci numbers
    a, b = START, NEXT
    count = 0

    # Handle invalid or zero input
    if n_terms <= 0:
        print("Please enter a positive integer.")

    # Handle the case when only one term is requested
    elif n_terms == 1:
        print(f"Fibonacci sequence up to {n_terms} term:")
        print(a)

    # Generate and print Fibonacci sequence for more than one term
    else:
        print(f"Fibonacci sequence up to {n_terms} terms:")
        while count < n_terms:
            print(a)
            a, b = b, a + b  # Update values for next Fibonacci number
            count += 1


def main():
    # Take the number of terms as input from the user
    try:
        n_terms = int(input("Enter the number of terms for Fibonacci sequence: "))

        # Call the Fibonacci function
        fibonacci_series(n_terms)

    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a positive integer.")


# Ensures main() runs only when the file is executed directly
if __name__ == "__main__":
    main()
