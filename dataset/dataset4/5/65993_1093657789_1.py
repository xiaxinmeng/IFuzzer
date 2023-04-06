print('#line {}: defining decorator'.format(lineno()))

def decorator(f):
    print('#  line {}: decorator called'.format(lineno()))
    print('#  line {}: defining inner'.format(lineno()))
    @functools.wraps(f)
    def inner(arg1, arg2):
        print('#    line {}: inner called, arg1 {} arg2 {}'.format(lineno(), arg1, arg2))
        for i, frame in enumerate(inspect.stack()):
            print("#      line {}: printed in inner, frame {}, name {}".format(lineno(), i, frame[3]))
        f(arg1 + 1 , arg2 + 1)