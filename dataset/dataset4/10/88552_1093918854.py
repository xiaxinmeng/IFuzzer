from importlib import util

mathmodule = util.find_spec("math")
math1 = util.module_from_spec(mathmodule)
print(math1.pi)