with TemporaryDirectory() as td:
    name = td.name
    print(os.path.exists(name))  # prints True

print(os.path.exists(name))  # prints False