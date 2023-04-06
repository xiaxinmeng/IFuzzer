f = open(fname, "rb")
print("len(f.read()): ", len(f.read()))
f.close()

f = open(fname, "rb")
for i in range(size):
        try:
                f.read(1)
        except IOError:
                print("IOError at byte %d" % i)
                break
f.close()