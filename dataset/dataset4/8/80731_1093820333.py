
try:
    raise ValueError()
except Exception as exc:
    e = exc
    __import__('pdb').set_trace()
