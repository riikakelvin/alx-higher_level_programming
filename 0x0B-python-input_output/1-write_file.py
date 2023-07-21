#!/usr/bin/python3
'''Defines a file-writing functin.'''

def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file/ doc
        text (str): The text to write to the file.
    Returns:
        The number of characters displayed.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
