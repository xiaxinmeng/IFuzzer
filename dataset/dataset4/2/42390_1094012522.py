a = 1
val = a
val = val + 1

a = [1]
val = a
val = val + [2]
# or
def f(val):
  val = val + [2]
f(a)