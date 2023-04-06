print('hello', end='', flush=True) # works fine
print('', end='', flush=True) # raises OSError as well