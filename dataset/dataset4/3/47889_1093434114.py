from warnings import warn

warn("hello world") # -> Success
warn(UserWarning)   # -> Segmentation fault
warn(None)          # -> Segmentation fault
warn(1)             # -> Segmentation fault