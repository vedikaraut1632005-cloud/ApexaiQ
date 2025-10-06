"""Prints an inverted triangle pattern of stars."""
def inverted_triangle(n):
    """Print inverted triangle with n rows."""
    for i in range(n, 0, -1):
        print("*" * i)

inverted_triangle(5)
