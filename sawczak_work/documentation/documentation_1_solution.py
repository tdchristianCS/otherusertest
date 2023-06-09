# Documentation practice  1

def remove_odd_numbers(numbers: list) -> list:
    """
    Take a list of numbers and return only the even ones.

    >>> remove_odd_numbers([1, 2, 3])
    [2]
    >>> remove_odd_numbers([3, 4, 6])
    [4, 6]
    """
    
    even_numbers = []

    for n in numbers:

        # If the number is even (divisible by 2)
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers

