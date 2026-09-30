"""A small collection of beginner-friendly utility functions."""


def is_palindrome(s):
    """Check whether a string is a palindrome.

    A palindrome reads the same forwards and backwards. This check ignores
    letter case, spaces, and punctuation, so "A man, a plan, a canal: Panama"
    counts as a palindrome.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    # Keep only letters and digits, and make everything lowercase
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    # Compare the cleaned text with its reverse
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count the number of words in a piece of text.

    Words are separated by whitespace (spaces, tabs, or new lines).

    Parameters:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text (0 for empty text).
    """
    # split() with no arguments splits on any whitespace
    # and ignores extra spaces automatically
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Uses the formula: F = C * 9/5 + 32

    Parameters:
        c (int or float): The temperature in degrees Celsius.

    Returns:
        float: The temperature in degrees Fahrenheit.
    """
    return c * 9 / 5 + 32


# Simple example calls to test the functions.
# This block only runs when the file is executed directly
# (python utils.py), not when it is imported.
if __name__ == "__main__":
    print("--- is_palindrome ---")
    print(is_palindrome("racecar"))                         # True
    print(is_palindrome("hello"))                           # False
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True

    print("\n--- count_words ---")
    print(count_words("Hello world"))                       # 2
    print(count_words("  Python   is   fun  "))             # 3
    print(count_words(""))                                  # 0

    print("\n--- celsius_to_fahrenheit ---")
    print(celsius_to_fahrenheit(0))                         # 32.0
    print(celsius_to_fahrenheit(100))                       # 212.0
    print(celsius_to_fahrenheit(-40))                       # -40.0