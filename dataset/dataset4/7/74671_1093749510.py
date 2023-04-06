set_cell = outer()
print(set_cell.__closure__[0].cell_contents)  # None
set_cell('something')
print(set_cell.__closure__[0].cell_contents)  # 'something'