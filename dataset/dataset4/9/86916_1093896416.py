a = tk.IntVar(name='a')
b = tk.IntVar(name='a')
assert a == b  # they refers to the same variable
assert a is not b  # but they are different objects
a.set(42); assert b.get() == a.get() == 42  # yes, it is the same variable
c = tk.IntVar(name='c', value=42)
assert c != a  # they are different variables
assert c.get() == a.get() == 42  # although having equal values
a.set(43); assert c.get() != a.get() == 43  # and setting one does not affect other