from datetime import datetime
from time import sleep
import sys

if __name__ == '__main__':
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