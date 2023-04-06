import os
import stat

s = os.stat(afile)

executable = (s.st_mode & stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH) == 0