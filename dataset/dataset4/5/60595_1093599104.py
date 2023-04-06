import logging.config

def my_handler(*args, **kwargs):
    h = logging.StreamHandler(*args, **kwargs)
    h.terminator = '!\n'
    return h

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            '()': my_handler,
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
}

logging.config.dictConfig(LOGGING)

logging.info('Hello')
logging.info('world')