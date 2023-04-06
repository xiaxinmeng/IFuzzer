
def cycle1(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

def cycle2(iterable):
    while True:
        for element in iterable:
              yield element
