my_sequence = [1, 2, 3, 4]
for i, item in zip(count(step=5), my_sequence):
    print(i, item)