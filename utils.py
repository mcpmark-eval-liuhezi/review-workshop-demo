"""Small Python utility collection."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def join_words(words):
    """Join a list of words with a comma and a space."""
    return ", ".join(words)


def greet(name):
    return "Hello, " + name


def average(numbers):
    return sum(numbers) / len(numbers)
