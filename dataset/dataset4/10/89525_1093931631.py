x = lambda a: len(a)
print(x.__code__.co_code)

#quickened
for _ in range(10):
 x('')

print(x.__code__.co_code)