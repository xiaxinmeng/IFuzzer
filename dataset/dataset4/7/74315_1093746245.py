print(pydoc.render_doc(Child))
print(pydoc.render_doc(c))
print(inspect.getdoc(c.sum)) # Need to patch getdoc before it checks for obj.__doc__ to check if the c.sum is an instance of partialmethod or partial
print(inspect.getdoc(Child.sum)) # Need to patch functools.partialmethod._make_unbound_method to copy the docs to _method