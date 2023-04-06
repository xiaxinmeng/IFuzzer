test1 = '''
str = "x" * 100000
lst = [str]
'''

test2 = '''
str = "x" * 100000
'''

print(timeit.timeit(test1, number=100000))
print(timeit.timeit(test2, number=100000))