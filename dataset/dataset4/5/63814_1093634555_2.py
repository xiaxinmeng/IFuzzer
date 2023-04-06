from distutils.core import setup, Extension
setup(name='PackageName',
      ext_modules=[Extension('foo', sources=['foo.c']),
                   Extension('bar', sources=['bar.c'])])