
import logging

class MyLogRecord(logging.LogRecord):
    def getMessage(self):
        print("Help! I am being formatted!")
        return super().getMessage()

logging.setLogRecordFactory(MyLogRecord)

logger = logging.getLogger("test")
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.StreamHandler())

logger.error("%d", 123)
