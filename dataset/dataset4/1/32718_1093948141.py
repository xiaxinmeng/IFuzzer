f = open("k.py", "w")
print >> f, "biglist = ["
for i in range(50000): print >> f, i, ","
print >> f, "]"
print >> f, "print len(biglist)"
f.close()