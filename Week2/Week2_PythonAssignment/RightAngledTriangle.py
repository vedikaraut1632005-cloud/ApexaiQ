"""Prints a right-angle triangle pattern of stars."""

def right_triangle(n):
    """Print right-angle triangle with n rows."""
    for i in range(1, n+1):
        print("*" * i)


right_triangle(9)

