"""Small helper utilities used by the workshop demo.

This module is intentionally plain: it exists to be reviewed, not to be clever.
"""


def slugify(text):
    # Turn a heading into a URL-friendly slug
    return "-".join(text.lower().split()).replace("--", "-")


def word_count(text):
    # Count the words in a string
    return len(text.split())


def clamp(value, low, high):
    # Keep a number inside [low, high]
    return max(low, min(high, value))
