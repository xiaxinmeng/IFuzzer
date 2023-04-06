from __future__ import print_function
import warnings

class MyClass:
    def __str__(self):
        return "A bad formatted string %(err)" % {"err" : "there is no %(err)s"}

class MyWarning(UserWarning):
    def __str__(self):
        return "A bad formatted string %(err)" % {"err" : "there is no %(err)s"}

try:
    warnings.warn("A bad formatted string %(err)" % {"err" : "there is no %(err)s"})
except ValueError as err:
    print("this exception is caught:", err)
try:
    warnings.warn(MyClass())
except ValueError as err:
    print("this exception is also caught:", err)

warnings.warn(MyWarning())

