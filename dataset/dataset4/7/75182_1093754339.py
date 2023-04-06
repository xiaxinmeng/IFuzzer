
median = median_low([(1, ['Anna']), (3, ['Paul', 'Henry']), (4, ['Kate'])], key=lambda elem: elem[0])
for name in median[1]:
    print(f"{name} is one of the people that reach the median score.")
