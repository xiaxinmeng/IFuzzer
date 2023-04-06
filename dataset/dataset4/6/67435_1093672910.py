import platform
if platform.system() == 'Windows':
    vcpath = os.environ['ProgramFiles']
    vcpath = os.path.join(vcpath, 'Common Files', 'Microsoft',
        'Visual C++ for Python', '9.0', 'vcvarsall.bat')
    if os.path.isfile(vcpath):
        import distutils.msvc9compiler
        old_find = distutils.msvc9compiler.find_vcvarsall
        def new_find(version):
            path = old_find(version)
            if path is None:
                return vcpath
        distutils.msvc9compiler.find_vcvarsall = new_find