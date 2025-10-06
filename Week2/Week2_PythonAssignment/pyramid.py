"""Prints a pyramid pattern of stars."""

def pyramid(n):
    """Print pyramid with n rows."""
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))

pyramid(5)
