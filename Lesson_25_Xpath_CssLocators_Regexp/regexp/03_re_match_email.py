"""
- The email address must start with one or more word characters
  (`\w`), dots (`.`), or hyphens (`-`).
- It must be followed by an `@` symbol.
- After the `@` symbol, there must be one or more word characters
  (`\w`), dots (`.`), or hyphens (`-`).
- It ends with a dot (`.`) followed by one or more word characters (`\w`).

"""
import re


def validate_email(email_address):
    """
    Validates the format of an email address using regular expressions.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # [a-zA-Z0-9_.-]
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{1,6}$'
    match = re.match(pattern, email_address)
    return True if match else False


if __name__ == "__main__":
    # Testing the validate_email function
    emails = (
        "test@example.com",
        "invalid_email",
        "user@domain",
        "info@domain.com",
        "info@@domain.com",
        "user.name@domain.co.uk"
    )

    for email in emails:
        if validate_email(email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is an invalid email address.")
