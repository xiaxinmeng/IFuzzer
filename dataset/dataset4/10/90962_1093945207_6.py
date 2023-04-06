
modules = [
    module
    for name, module in sys.modules.items()
    if "common_object" in name
]
print(len(modules)) # 2
print(modules[0].__file__ == modules[1].__file__) # True
