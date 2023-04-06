compiler_class = { 'unix':    ('unixccompiler', 'UnixCCompiler',
                               "standard UNIX-style compiler"),
                   'msvc':    ('_msvccompiler', 'MSVCCompiler',
                               "Microsoft Visual C++"),
                   'cygwin':  ('cygwinccompiler', 'CygwinCCompiler',
                               "Cygwin port of GNU C Compiler for Win32"),
                   'mingw32': ('cygwinccompiler', 'Mingw32CCompiler',
                               "Mingw32 port of GNU C Compiler for Win32"),
                   'bcpp':    ('bcppcompiler', 'BCPPCompiler',
                               "Borland C++ Compiler"),
                 }