print("Hello, World!")
print("This is a project.")

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




def main():
    # Example usage
    fraction1 = (1, 3)  # 1/2
    fraction2 = (1, 6)  # 1/3

    result = add_fractions(fraction1, fraction2)
    print(f"The sum of {fraction1} and {fraction2} is: {result[0]}/{result[1]}")


if __name__ == "__main__":
    main()
     