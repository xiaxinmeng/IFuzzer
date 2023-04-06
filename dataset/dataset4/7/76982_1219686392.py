
import timeit
def f(arr):
    return all(value == '' for value in arr)

def g(arr):
    for value in arr:
        if value != '':
            return False
    return True

to_convert = ["" for i in range(50)]

for i in range(4):
    print('using all:\n', timeit.repeat("f(to_convert)", globals=globals()))
    print('using loop:\n', timeit.repeat("g(to_convert)", globals=globals()))
