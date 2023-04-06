class Windows27VS9Build(WindowsBuild):
    buildersuffix = 'vs9'
    build_command = [r'PC\VS9.0\build.bat', '-e', '-k', '-d']
    test_command = [r'PC\VS9.0\rt.bat', '-q', '-d', '-uall', '-rwW', '--slowest']
    clean_command = [r'PC\VS9.0\build.bat', '-t', 'Clean', '-d']
    python_command = [r'PC\VS9.0\python_d.exe']


class Windows6427VS9Build(Windows27VS9Build):
    test_command = [r'PC\VS9.0\rt.bat', '-x64', '-q', '-d', '-uall', '-rwW', '--slowest']
    buildFlags = ['-p', 'x64']
    cleanFlags = ['-p', 'x64']
    python_command = [r'PC\VS9.0\amd64\python_d.exe']