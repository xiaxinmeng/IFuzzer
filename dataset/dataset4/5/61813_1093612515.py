fid = open('/tmp/bigfile.py', 'w')
L = '\n'.join(map(lambda x: "#%i\n'%i'\n" % (x,x), range(10000)))
fid.writelines(L)
fid.close()