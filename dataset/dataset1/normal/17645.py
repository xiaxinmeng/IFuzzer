big = 1073741824
x = "__" + "s" * big
type("X" * big, (), {"__slots__": x})
