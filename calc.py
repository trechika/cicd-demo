def add(a, b):
    return a - b  # bug: should be a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
