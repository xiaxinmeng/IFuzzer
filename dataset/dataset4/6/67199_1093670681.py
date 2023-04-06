import logging
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
        },
    },
}

print('Starting: %s' % sys.version)
from logging.config import dictConfig
dictConfig(LOGGING)
print('After dictconfig')
print('_handlerList 1, initial:', logging._handlerList, len(logging._handlers))
import importlib
print('_handlerList 2, about to import shutil:', logging._handlerList, len(logging._handlers))
import shutil
print('_handlerList 3, just imported shutil:', logging._handlerList, len(logging._handlers))
print('')