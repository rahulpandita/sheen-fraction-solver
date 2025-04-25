
def add_fractions(fraction1, fraction2):
    """
    Adds two fractions together.

    Args:
        fraction1 (tuple): The first fraction as a tuple (numerator, denominator).
        fraction2 (tuple): The second fraction as a tuple (numerator, denominator).

    Returns:
        tuple: The sum of the two fractions as a tuple (numerator, denominator).
    """
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2

    # Find a common denominator
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1

    # Add the numerators
    result_numerator = new_numerator1 + new_numerator2

    # convert to lowest terms
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisor = gcd(result_numerator, common_denominator)
    result_numerator //= common_divisor
    common_denominator //= common_divisor
    # Return the result as a tuple
    return result_numerator, common_denominator


def get_fraction_input():
    """
    Prompts the user for a fraction input.

    Returns:
        tuple: The fraction as a tuple (numerator, denominator).
    """
    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            if denominator == 0:
                raise ValueError("Denominator cannot be zero.")
            return numerator, denominator
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    
    fraction1 = get_fraction_input()
    fraction2 = get_fraction_input()
    print(f"Adding fractions: {fraction1} and {fraction2}")

    result = add_fractions(fraction1, fraction2)
    print(f"The sum of {fraction1} and {fraction2} is: {result[0]}/{result[1]}")


if __name__ == "__main__":
    main()
     