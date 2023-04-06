
extensions = [..., 'sphinx.ext.doctest', ...]

doctest_global_setup = '''
try:
    import _tkinter
except ImportError:
    _tkinter = None
'''
