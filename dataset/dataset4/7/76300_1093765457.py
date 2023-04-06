def get_code(self, fullname):
    ...
    st = self.path_stats(source_path)
    ...
    source_mtime = int(st['mtime']) <~~~~~~ HERE
    ...

def path_stats(self, path):
    st = _path_stat(path)
    return {'mtime': st.st_mtime, 'size': st.st_size}

def _path_stat(path):
    return _os.stat(path)