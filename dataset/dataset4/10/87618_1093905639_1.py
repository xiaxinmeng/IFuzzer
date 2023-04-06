class C:
    pass

for i in range(20):
    setattr(C, f"f{i}", lambda self: None)