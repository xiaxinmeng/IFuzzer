
data = [1, 3, 4]
median = median_low(enumerate(data), key=lambda elem: elem[1])
print(f"median is at position {median[0]}")
