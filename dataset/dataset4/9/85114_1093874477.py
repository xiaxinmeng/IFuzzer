
import logging
from multiprocessing.managers import BaseManager

class SimpleGenerator:
    def __init__(self, obj): self._obj = obj
    def __call__(self): return self._obj

def get_logger_proxy(logger):
    class LoggerManager(BaseManager): pass
    logger_generator = SimpleGenerator(logger)
    LoggerManager.register('logger', callable = logger_generator)
    logger_manager = LoggerManager()
    logger_manager.start()
    logger_proxy = logger_manager.logger()

    return logger_proxy

logger = logging.getLogger('test')

logger_proxy = get_logger_proxy(logger)
