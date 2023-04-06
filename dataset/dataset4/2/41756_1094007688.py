def get_cell_value(cell):
    return type(lambda: 0)(
        (lambda x: lambda: x)(0).func_code, {}, None,
None, (cell,)
    )()