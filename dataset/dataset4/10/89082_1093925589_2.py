print(type(UserDict))  # <class 'typing._TypedDictMeta'>
print(UserDict.__instancecheck__(UserDict, {}))  # TypeError: TypedDict does not support instance and class checks