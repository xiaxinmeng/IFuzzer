import msvcrt
fp = open('file.txt', 'w')
msvcrt.locking(fp.fileno(), msvcrt.LK_NBLCK, -1)
print('End')