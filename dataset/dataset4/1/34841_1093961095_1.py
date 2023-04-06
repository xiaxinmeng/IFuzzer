prog = os.path.splitext(os.path.basename(src))[0] 
if sys.platform == 'win32': prog = prog + '.exe'
self.temp_files.append(prog)