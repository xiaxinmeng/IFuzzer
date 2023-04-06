print(ini['section A']['key 1'])    # OK
print(ini['section A']['(key 1)'])  # Raises KeyError