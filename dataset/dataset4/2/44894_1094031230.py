sqlite_libfile = self.compiler.find_library_file(                      
           
                     sqlite_dirs_to_check + lib_dirs, 'sqlite3')
sqlite_libdir = [os.path.abspath(os.path.dirname(sqlite_libfile))]
                                                                       
       