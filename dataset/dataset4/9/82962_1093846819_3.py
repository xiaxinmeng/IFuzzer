
import collections
import logging
from logging.handlers import MemoryHandler


class DequeMemoryHandler(MemoryHandler):

    def __init__(self, capacity, *args, **kwargs):
        super().__init__(capacity, *args, **kwargs)
        self.buffer = collections.deque(maxlen=capacity)

    def shouldFlush(self, record):
        return record.levelno >= self.flushLevel


handler = DequeMemoryHandler(capacity=5, target=logging.StreamHandler())
logging.basicConfig(level=logging.INFO, handlers=[handler])

for i in range(1, 21):
    logging.info('Spam %d', i)
    if i % 10 == 0:
        logging.error(f'---> Eggs {i}')
