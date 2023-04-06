
pid, sts = os.waitpid(pid, 0)
...
if sts:
    self.log_error("CGI script exit status %#x", sts)
