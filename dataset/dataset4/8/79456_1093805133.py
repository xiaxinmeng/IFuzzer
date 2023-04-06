current_umask = os.umask(0)  # line1
os.umask(current_umask)      # line2
return current_umask