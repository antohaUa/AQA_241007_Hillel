"""
My first program.

Flow:
  - print copyright
  - get first and last name form input
  - print formatted Hello string
"""
YEAR = 2023
COPYRIGHT = f'© {YEAR}'


def format_name(first_name, last_name):
    """
    Format a person's name using f-strings.

    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.

    Returns:
        str: The formatted name.
    """
    return f'Hello: {last_name}, {first_name}!\n{COPYRIGHT}'


print(COPYRIGHT)
inp_first_name = input('First name: ')
inp_last_name = input('Last name: ')
print(format_name(inp_first_name, inp_last_name))
