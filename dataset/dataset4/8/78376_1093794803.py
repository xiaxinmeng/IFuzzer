import nt, sys; assert sys.executable.startswith(nt._getvolumepathname(sys.executable))