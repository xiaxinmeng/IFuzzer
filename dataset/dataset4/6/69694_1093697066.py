
import logging

class H(logging.Handler):
    def emit(self, record):
        print(record.args, type(record.args))

lgr = logging.getLogger()
lgr.addHandler(H())
lgr.error("msg", 1)
lgr.error("msg", dict(a=1))
lgr.error("msg", dict(a=1), 2)
