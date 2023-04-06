import sys
print(sys.gettotalrefcount())
sp = super(int, 1)
for i in range(100000):
  super.__init__(sp, float, 1.0)
print(sys.gettotalrefcount())
