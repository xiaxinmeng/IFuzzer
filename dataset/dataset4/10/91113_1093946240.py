
import copy
import logging

# Some module we don't control
oldLogger = logging.getLogger("abc")

# Some module where we want to change over to custom logging
class MyLogger(logging.Logger):
    pass

# Override the manager, root, etc., so everything uses our class
logging.setLoggerClass(MyLogger)
logging.root = root = MyLogger("", logging.WARNING)
logging.Logger.manager = logging.Manager(root)

newLogger = logging.getLogger("def")

# Later on this happens, which internally calls __reduce__
copy.deepcopy(oldLogger)
