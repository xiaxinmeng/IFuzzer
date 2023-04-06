def f(**kwargs):
    kwargs["spam"] = False

kwargs = {"spam": True}
f(**kwargs)
assert kwargs["spam"]