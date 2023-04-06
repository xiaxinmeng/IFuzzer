if self.distribution.has_data_files():
    for item in self.distribution.data_files:
        if isinstance(item, basestring): # plain file
            self.filelist.append(convert_path(item))
        else: # an (outdir, files) tuple
            outdir,data_files = item
            self.filelist.extend(convert_path(f) for f in data_files)