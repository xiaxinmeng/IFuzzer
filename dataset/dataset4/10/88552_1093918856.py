from importlib import util

mathmodule = util.find_spec("math")
math1 = util.module_from_spec(mathmodule)
mathmodule.loader.exec_module(math1)
print(math1.pi)