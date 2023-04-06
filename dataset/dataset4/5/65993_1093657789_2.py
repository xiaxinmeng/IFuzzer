print('#line {}: defining wrapped'.format(lineno()))

@decorator
def wrapped(warg1, warg2):
    print('#  line {}: wrapped called, warg1 {} warg2 {}'.format(lineno(), warg1, warg2))
    print("#  line {}: printed in wrapped, wrapped.__name__ == {}".format(lineno(), wrapped.__name__))
    stack = inspect.stack()
    for i, frame in enumerate(stack):
        print("#    line {}: printed in wrapped, frame {}, name {}".format(lineno(), i, frame[3]))

print('#line {}: Calling wrapped...'.format(lineno()))
wrapped(1,2)

print("#line {}: done".format(lineno()))