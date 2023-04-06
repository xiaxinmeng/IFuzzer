
for j in set(dir(type(l))) - set(dir(l)):
    print(f'l.{j}.__qualname__')
