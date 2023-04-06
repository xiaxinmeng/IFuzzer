import logging.config
import sys

d = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {
        'level': 'DEBUG',
    }
}

logging.config.dictConfig(d)
logging.debug('%s', sys.version)