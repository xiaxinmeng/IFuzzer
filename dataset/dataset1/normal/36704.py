import os
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
for name in os.listdir():
    logging.error('Hypothetical syntax error at line 1 of file: {}'.format(name))
