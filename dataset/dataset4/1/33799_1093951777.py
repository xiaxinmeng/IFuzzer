if (self.compiler.find_library_file(lib_dirs, 'readline')):
            exts.append( Extension('readline', ['readline.c'],
                                   libraries=['readline', 'termcap']) )