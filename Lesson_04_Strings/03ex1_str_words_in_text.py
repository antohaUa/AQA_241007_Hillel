import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')


def count_words(text: str) -> int:
    """
    Given a multi-line text, calculate the number of words in it.

    Args:
    text (str): A multi-line string containing one or more words.

    Returns:
    int: The total number of words in the multi-line text.
    """
    words = text.strip().split()  # Split the text into words
    # print(words)
    count = len(words)  # Count the number of words
    logging.info(f'Number of words in given text: {count}')  # Log the result
    return count


# Example usage
input_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nullam urna odio, efficitur sit amet sollicitudin vel, commodo nec purus.
Mauris ornare neque eget dictum bibendum dfsdf fsdfasd.     
"""

count_words(input_text)
