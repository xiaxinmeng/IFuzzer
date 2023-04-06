import itertools

def count(offset=0,stride=1):
    for i in itertools.count():
        yield offset+i*stride


# this version probably performs faster
def count(offset=0,stride=1):
    while True:
        yield offset
        offset += stride