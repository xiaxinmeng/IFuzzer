# Ugly hack so I can run setup.py in my IDE
sys.argv = ['setup.py', 'build_ext', '--inplace']

# Init include dirs
include_dirs = ['.']
include_dirs.extend(get_numpy_include_dirs())

# Creat Extensions
ext_modules = [
     Extension('test_', ['test_.pyx'],
        include_dirs=include_dirs,
        ),
     ]

# Compile
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    )

print('Successfully compiled cython file: test_')