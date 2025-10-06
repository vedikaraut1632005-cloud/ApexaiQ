"""Program to check if a string is palindrome."""

def is_palindrome(s):
    """Check if a string reads the same forward and backward."""
    return s == s[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
