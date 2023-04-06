def delete_chosen_variable(name):
    del globals()[name]
    gv = 'local here'
    print(locals())

delete_chosen_variable('gv')