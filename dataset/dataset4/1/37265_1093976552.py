_print_exc(file=s)
_sys.stderr.write("Exception in thread %s:\n%s\n" %
                       (self.getName(), s.getvalue()))