import logging
import unittest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestLogging(unittest.TestCase):
    def test_logging(self):
        with self.assertLogs(level=logging.WARNING):
            logger.info('foo')