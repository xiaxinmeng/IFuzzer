def filecount(self):                                                                                         
    """Return total count of files in the archive."""                                                        
    return len(self.filelist)                                                                                
                                                                                                                 
def total_compressed_size(self):                                                                             
    """Return total compressed size in the archive."""                                                       
    return sum([data.compress_size for data in self.filelist])                                               
                                                                                                                 
def total_uncompressed_size(self):                                                                           
    """Return total uncompressed size in the archive."""                                                     
    return sum([data.file_size for data in self.filelist])