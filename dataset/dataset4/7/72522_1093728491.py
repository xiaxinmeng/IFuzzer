import logging
import logging.config
import sys

def main():
    config = {
        'version': 1,
        'formatters': {
            'default': {
                '()': 'foo',
            },
        }
    }
    logging.config.dictConfig(config)


if __name__ == '__main__':
    sys.exit(main())