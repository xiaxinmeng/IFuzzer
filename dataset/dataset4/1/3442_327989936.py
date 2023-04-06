
for i in range(128):
    print('{:d}, '.format(chr(i) in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"), end='')
    if i % 16 == 15:
        print()
