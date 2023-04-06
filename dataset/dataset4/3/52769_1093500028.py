def handleRmtreeError(func, path, exc):
  excvalue = exc[1]
  if excvalue.errno == errno.EACCES:
    if func in (os.rmdir, os.remove):
      parentpath = path.rpartition('/')[0]
      os.chmod(parentpath, stat.S_IRWXU) # 0700
      func(path)
    elif func is os.listdir:
      os.chmod(path, stat.S_IRWXU) # 0700
      rmtree(path=path, ignore_errors=False, onerror=handleRmtreeError)
  else:
      raise