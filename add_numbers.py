def add_numbers(a, b):
    """
    Adds two numbers together.

    Args:
        a (int or float): The first number to add
        b (int or float): The second number to add

    Returns:
        int or float: The sum of a and b

    Raises:
        TypeError: If either a or b is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b

if __name__ == "__main__":
    # Example usage
    result = add_numbers(5, 3)
    print("5 + 3 =", result)  # Outputs: 8