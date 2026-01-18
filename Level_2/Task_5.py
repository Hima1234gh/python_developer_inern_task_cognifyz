"""Write a Python program that reads a text
file and counts the occurrences of each
word in the file. Display the results in
alphabetical order along with their
respective counts."""


import re  # Used for regular expression operations


def clean_word(text: str) -> str:
    """
    Removes punctuation and special characters from the text.
    Keeps only lowercase letters, digits, and whitespace.
    """
    return re.sub(r"[^\w\s\_]", "", text)


def count_word_in_file(filepath: str) -> dict:
    """
    Reads a text file and counts the occurrence of each word.
    Returns a dictionary with words as keys and counts as values.
    """
    word_count: dict[str, int] = {}

    try:
        # Open the file in read mode
        with open(filepath, "r") as f:
            # Read file content and convert to lowercase
            text: str = f.read().lower()
    except FileNotFoundError as e:
        # Handles case when file does not exist
        print(f"Error : {e}")
        return {}
    except IOError as e:
        # Handles other file reading errors
        print(f"Error : {e}")
        return {}

    # Clean the text by removing punctuation
    clear_text: str = clean_word(text)

    # Split cleaned text into individual words
    words: list[str] = clear_text.split()

    # Count each word's occurrence
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def main():
    # Take file path input from the user
    file_path: str = input("Enter the file path : ")

    # Get word count dictionary from the file
    word_count: dict = count_word_in_file(file_path)

    # Display words in alphabetical order with their counts
    for word in sorted(word_count.keys()):
        print(f"{word} : {word_count[word]}")


# Ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
