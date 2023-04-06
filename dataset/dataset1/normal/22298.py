from sys import stderr                      
from warnings import warn
                     
stderr.close()
try:
    warn("foo")
except ValueError as e:
    print(e)
