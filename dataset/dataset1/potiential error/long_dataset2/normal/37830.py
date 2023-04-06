def simple():
    for number in range(2):
        try:
            return number
        finally:
            continue

simple()
