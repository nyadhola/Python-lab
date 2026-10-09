
# Utility functions for the Python Lab project.

def square(n):
    """Return the square of a number."""
    return n * n


def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32