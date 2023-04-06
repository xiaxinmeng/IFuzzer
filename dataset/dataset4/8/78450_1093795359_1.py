logger1 = logging.getLogger('abc')
logger2 = logging.getLogger('cde')

logger1.setLevel(logging.ERROR)
logger2.setLevel(logging.ERROR)

print("logging error : ", logger1.isEnabledFor(logging.ERROR))

print("logger dict : ", logging.Logger.manager.loggerDict)

print("clearing logging dict ")
logging.Logger.manager.loggerDict.clear()
print("logger dict : ", logging.Logger.manager.loggerDict)
print("logging enabled for error : ", logger1.isEnabledFor(logging.ERROR))

if sys.version_info >= (3,7):
    # Since we clear logging.Logger.manager.loggerDict.clear() the cache is not reset
    print("Cache ", logger1._cache)

print("Setting to critical")
logger1.setLevel(logging.CRITICAL)
if sys.version_info >= (3,7):
    print("Cache after setting to critical ", logger1._cache)
print("logging enabled for error : ", logger1.isEnabledFor(logging.ERROR))