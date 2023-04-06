import sys
print(sys.argv)
try:
    open(sys.argv[1]).close()
except Exception as err:
    print("open error: %s" % err)
else:
    print("open ok")