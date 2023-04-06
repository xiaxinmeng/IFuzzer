def simple(x):
    for number in range(2):
        try:
            return number
        finally:
            if x:
                continue

print(simple(0))
print(simple(1))