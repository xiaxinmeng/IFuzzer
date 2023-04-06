import logging
import StringIO
stream = StringIO.StringIO()
h = logging.StreamHandler(stream)
r = logging.getLogger()
r.addHandler(h)
#Do your testing work
r.removeHandler(h)
h.close() # closes underlying stream, also removes logging refs to h