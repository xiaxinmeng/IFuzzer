a = {0: 0}
it = iter(a.values())
print('Length hint:', it.__length_hint__())
print(next(it))
print('Length hint:', it.__length_hint__())
del a[0]
a[1] = 99
print(next(it))
print('Length hint:', it.__length_hint__())