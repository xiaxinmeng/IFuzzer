import mimetypes

print(mimetypes.types_map.get('.gz'))  # None
mimetypes.init()  # <- initialize
print(mimetypes.types_map.get('.gz'))  # application/gzip