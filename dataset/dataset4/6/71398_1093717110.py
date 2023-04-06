with open('out.xxx', 'wb') as fp:
    fp.write('x' * (1024*1024*64))
    fp.write('\n')