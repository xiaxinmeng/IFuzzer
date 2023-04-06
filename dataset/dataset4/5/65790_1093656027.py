c = '''
def g():
    def f():
        if True:
            exec("", {}, {})
'''
compile(c, "<code>", "exec")