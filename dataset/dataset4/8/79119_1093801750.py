from mimetypes import init, types_map

print(types_map.get('.gz'))  # None
init()  # <- initialize
print(types_map.get('.gz'))  # None