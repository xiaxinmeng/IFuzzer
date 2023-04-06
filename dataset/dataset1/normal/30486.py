def outer():
    cell = None
    def inner(ob):
        nonlocal cell
        cell = ob  # rebinds <hidden-cell>.cell_contents
    return inner

set_cell = outer()
print(set_cell.__closure__[0].cell_contents)  # None
set_cell('something')
print(set_cell.__closure__[0].cell_contents)  # 'something'
