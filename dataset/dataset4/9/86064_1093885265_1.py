def set_up_logger(app_name, level=logging.INFO, file="test.log"):
    formatter = logging.Formatter(LOG_FORMAT)
    log = logging.getLogger(app_name)
    # The next line lets the test pass
    log.setLevel(level)
    return log

logger = set_up_logger(__name__)

class TestLogging(unittest.TestCase):
    def test_logging(self):
        with self.assertLogs(level=logging.WARNING):
            logger.info('foo')