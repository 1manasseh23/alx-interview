#!/usr/bin/python3
"""This a method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check if the most significant bit is set
        if num & 0x80 == 0:
            # If num_bytes is greater than 0, then this is an invalid encoding
            if num_bytes > 0:
                return False
        else:
            # If num_bytes is 0, then this is the start of a new character
            if num_bytes == 0:
                # Count the number of leading ones
                # to determine the number of bytes
                mask = 0x80
                while num & mask:
                    num_bytes += 1
                    mask >>= 1

                # An invalid number of bytes
                if num_bytes == 0 or num_bytes > 4:
                    return False
            else:
                # This is not the start of a new character,
                # so it should be a continuation byte
                if num >> 6 != 0b10:
                    return False

            # Decrement the number of bytes remaining for the current character
            num_bytes -= 1

    # All bytes have been validated
    return num_bytes == 0
