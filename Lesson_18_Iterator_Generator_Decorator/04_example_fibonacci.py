def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to a given number 'n'.

    Args: n (int): The upper limit for the Fibonacci sequence.
    Yields: int: The next number in the Fibonacci sequence.
    Returns: None
    """
    a, b = 0, 1  # Start with the first two numbers in the sequence
    while a <= n:
        yield a
        a, b = b, a + b  # Update the current and next numbers


# Using the generator function
num = 3000
sequence = fibonacci_sequence(num)

print(f'Fibonacci sequence up to {num}:')
for number in sequence:
    print(number, end=' ')
print()
