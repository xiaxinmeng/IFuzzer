items = [1, 2, 3, 4, 5]
for index, value in enumerate(items):
    print(f"index: {index}, value: {value}, items: {items}")
    if value == 2:
        x = items.pop(index)
        print(f"after popping 2: {items}")