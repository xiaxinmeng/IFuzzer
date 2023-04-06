size = 8*1024
for i in range(1, 120):
    print('Step %d ' % i, format(size, ','), 'bytes')
    size = size + (size >> 3) + 6