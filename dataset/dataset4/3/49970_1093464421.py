if platform.system() == "Windows":
    metadata["creation time"] = s.st_ctime
else:
    metadata["unix ctime"] = s.st_ctime