#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Return number of minimum operations to
    copy and paste a single character 'H' to give
    the required 'n' characters of 'H'.

    arg: `n`
    """

    if n <= 1:
        return 0

    text_file_chars = 'H'

    copied_text = text_file_chars
    op_count = 1

    # while the len of text_file chars is not upto n
    while len(text_file_chars) < n:
        if len(text_file_chars) != 1 and not n % len(text_file_chars):
            copied_text = text_file_chars
            op_count += 1

        # paste
        text_file_chars += copied_text
        op_count += 1

    return op_count
