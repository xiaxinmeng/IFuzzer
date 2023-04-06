print('example 2'.center(30, '='))
for item in map(raise_stop_iteration, range(10, 20)):
    print(item)
print('end of example 2'.center(30, '='))