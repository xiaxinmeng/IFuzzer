def f():
    l = []
    l.append(slice(l))
# Will consume memory without bound:
while True:
    f()