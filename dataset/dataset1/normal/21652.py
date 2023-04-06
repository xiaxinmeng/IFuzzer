import mimetypes
mimetypes.init()
for key,value in mimetypes.types_map.items():

    print(repr(key), repr(value))
    break
