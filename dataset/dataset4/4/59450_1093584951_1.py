nan_name = repr(float('nan'))
ast.literal_eval(nan_name) # ValueError

inf_name = repr(float('inf'))
ast.literal_eval(inf_name)  # ValueError

ast.literal_eval("2e308") # == inf