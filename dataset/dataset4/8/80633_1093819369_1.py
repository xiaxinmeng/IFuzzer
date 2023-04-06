a = {0: 0}
it = iter(a)
print('Length hint:', it.__length_hint__())
next(it)
print('Length hint:', it.__length_hint__())
del a[0]
a[1] = 0
next(it)
print('Length hint:', it.__length_hint__())