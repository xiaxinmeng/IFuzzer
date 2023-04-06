
import pkgutil

import foo


for _, mod, _ in pkgutil.walk_packages(foo.__path__, foo.__name__ + '.'):
    print(mod)
