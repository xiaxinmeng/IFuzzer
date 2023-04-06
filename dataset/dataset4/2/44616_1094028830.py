setattr(obj, '__mul__', new_mul)
obj *= 1 # __mul__ will be called.
# But
obj.__mul__(1) # new_mul will be called.