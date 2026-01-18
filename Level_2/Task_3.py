"""Create a Python function that evaluates
the strength of a password entered by the
user. Implement checks for factors such as
length, presence of uppercase and
lowercase letters, digits, and special
characters."""

import re  # Import regex module for pattern matching

# Precompiled regular expressions
# These are compiled once and reused for efficiency

DIGIT = re.compile(r'\d')          # Matches any digit (0–9)
UPPERCASE = re.compile(r'[A-Z]')   # Matches any uppercase letter
LOWERCASE = re.compile(r'[a-z]')   # Matches any lowercase letter
SPECIAL_CHAR = re.compile(r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>/?|]")  # Matches allowed special characters


 
# Individual validation functions
# Each function checks a single password rule
# Returns True if rule is satisfied, else False
 

def digit_check(password: str) -> bool:
    """Check if password contains at least one digit."""
    return bool(DIGIT.search(password))


def uppercase_check(password: str) -> bool:
    """Check if password contains at least one uppercase letter."""
    return bool(UPPERCASE.search(password))


def lowercase_check(password: str) -> bool:
    """Check if password contains at least one lowercase letter."""
    return bool(LOWERCASE.search(password))


def special_char_check(password: str) -> bool:
    """Check if password contains at least one special character."""
    return bool(SPECIAL_CHAR.search(password))


 
# Validator configuration dictionary
# Maps each rule to:
# - its checking function
# - an error message if the rule fails
 

VALIDATORS = {
    "digit": {
        "check": digit_check,
        "message": "Password must contain at least one digit."
    },
    "uppercase": {
        "check": uppercase_check,
        "message": "Password must contain at least one uppercase letter."
    },
    "lowercase": {
        "check": lowercase_check,
        "message": "Password must contain at least one lowercase letter."
    },
    "special_char": {
        "check": special_char_check,
        "message": "Password must contain at least one special character."
    }
}


 
# Core password strength evaluation function
# Returns:
# - A descriptive error message if a rule fails
# - "Password is strong." if all rules pass
 

def strength_check(password: str) -> str:
    """Evaluate the strength of the given password."""

    # Check minimum length requirement
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."

    # Apply each validator rule sequentially
    for rule in VALIDATORS.values():
        if not rule["check"](password):
            return rule["message"]

    # All checks passed
    return "Password is strong."


 
# Main program loop
# Keeps asking for input until a strong password is entered
 

def main():
    while True:
        password = input("Enter your password: ")
        result = strength_check(password)
        print(result)

        # Exit loop once a strong password is provided
        if result == "Password is strong.":
            break


 
# Entry point of the program
# Ensures main() runs only when file is executed directly
 

if __name__ == "__main__":
    main()
