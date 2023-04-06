
import timeit

MAX = 10000000


start = timeit.default_timer()
for i in range(MAX):
    _raw_input()

end = timeit.default_timer()

print('estimated : {}'.format(end - start))

