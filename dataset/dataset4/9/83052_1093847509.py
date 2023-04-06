data = [1, 2, 3, 4, 5]
x = filter(lambda x: True if x > 2 else False, data)
print(x)