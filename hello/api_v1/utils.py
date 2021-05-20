def add(a, b):
    if isinstance(a, str):
        a = int(a)

    if isinstance(b, str):
        b = int(b)

    return a + b
