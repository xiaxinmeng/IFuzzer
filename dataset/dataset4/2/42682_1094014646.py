import os
if not (os.path.isfile(fname)):
   raise IOError('Provided filename is not existing')