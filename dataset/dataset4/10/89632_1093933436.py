# begin of CODE
def aa(x):
    print("aa")
def bb(x):
    print("bb")

namefun = [
    ("a", aa),
    ("b", bb),
]
name2fun = {}
for name, fun in namefun:
    name2fun[name] = lambda x: fun(x)
# issue happened when calling lambda
name2fun["a"](1)
name2fun["b"](1)
# end of CODE