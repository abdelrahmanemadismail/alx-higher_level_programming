#!/usr/bin/python3


def text_indentation(text):
    """
    This function prints the given text with two newlines after each of
    the characters '.', '?', and ':'.

    param text: A string containing the text to be processed.
    type text: str

    raises TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    need_newline = True

    for char in text:
        if char in '.?:':
            if need_newline:
                result += '\n\n'
            else:
                result += char
            need_newline = False
        else:
            result += char
            need_newline = True

    print(result)
