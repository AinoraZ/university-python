import doctest


def is_perfect_number(number: int) -> bool:
    """Return boolean whether number is perfect number
    >>> is_perfect_number("Hello")
    False
    >>> is_perfect_number(['h','e','l','l','o'])
    False
    >>> is_perfect_number(33.2)
    False
    >>> is_perfect_number(28.2)
    False
    >>> is_perfect_number(33)
    False
    >>> is_perfect_number(2)
    False
    >>> is_perfect_number(3)
    False
    >>> is_perfect_number(6)
    True
    >>> is_perfect_number(28)
    True
    >>> is_perfect_number(496)
    True
    >>> is_perfect_number(6.0)
    True
    """
    try:
        converted = int(number)
        if converted != number:
            return False
    except (ValueError, TypeError):
        return False

    if converted <= 0:
        return False

    divisor_sum = 0
    for divisor in range(1, converted):
        if converted % divisor is 0:
            divisor_sum += divisor

    return converted == divisor_sum


if __name__ == "__main__":
    doctest.testmod()
