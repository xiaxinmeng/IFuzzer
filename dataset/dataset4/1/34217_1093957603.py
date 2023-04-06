def get_free_space(path = '.'):
   """
      Determine the free space in bytes for the given path.
   """
   if sys.platform == "win32":
      sizes = win32file.GetDiskFreeSpace(path)
      return sizes[0] * sizes[1] * sizes[2]
   else:
      status = os.statvfs(path)
      return status[statvfs.F_BAVAIL] * status[statvfs.F_FRSIZE]



def get_partition_size(path = '.'):
   """
      Determine the total space in bytes for the given path.
   """
   if sys.platform == "win32":
      sizes = win32file.GetDiskFreeSpace(path)
      return sizes[0] * sizes[1] * sizes[3]
   else:
      status = os.statvfs(path)
      return status[statvfs.F_BLOCKS] * status[statvfs.F_FRSIZE]