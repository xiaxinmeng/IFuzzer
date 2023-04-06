import builtins
builtins.__dict__['__debug__'] = 'Surprise!'
builtins.__dict__['None'] = 'Surprise!'

print(__debug__)
print(None)