import re, timeit, functools, sys

def re_test_true(string):
    print("testing string len: ", len(string))
    re.search(r'^A', string)

def re_test_false(string):
    print("testing string len: ", len(string))
    re.search(r'^x', string)

print(sys.version)

huge_string = 'A' * 100000
print('re_test_false: ', timeit.timeit(functools.partial(re_test_false, huge_string), number=1))

huge_string = 'A' * 1000000000
print('re_test_false: ', timeit.timeit(functools.partial(re_test_false, huge_string), number=1))