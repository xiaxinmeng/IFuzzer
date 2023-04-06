res = root.tk.call('wm', 'overrideredirect', root._w, True)
print([res.typename])
print([res.string])