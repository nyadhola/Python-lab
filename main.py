
# Main program for the Python Lab project.

from utils import square, is_even, celsius_to_fahrenheit


def main():
    """Ask the user for a number and display the results."""
    try:
        number = int(input("Enter a whole number: "))

        print(f"The square of {number} is {square(number)}.")

        if is_even(number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")

        fahrenheit = celsius_to_fahrenheit(number)
        print(
            f"{number} degrees Celsius is "
            f"{fahrenheit} degrees Fahrenheit."
        )

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()