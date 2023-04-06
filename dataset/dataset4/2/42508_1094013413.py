longexpr = 'x = x or ' + '-x' * 2500
code = '''
def f(x):
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    while x:
        x -= 1
        # EXTENDED_ARG/JUMP_ABSOLUTE here
    return x
''' % ((longexpr,)*10)