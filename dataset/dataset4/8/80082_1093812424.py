import json;

def default(o):
    out = repr(o).encode()
    print(id(out))
    if len(out) > 100:
        print(out)
        return "string"
    return out