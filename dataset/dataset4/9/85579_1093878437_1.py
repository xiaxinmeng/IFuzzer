print('example 1'.center(30, '='))
for item in map(raise_stop_iteration, range(5)):
    print(item)
print('end of example 1'.center(30, '='))