
import datetime
import logging.handlers
import logging
import time

fn = 'test_file'
now = datetime.datetime.now()
handlers = [
    logging.handlers.TimedRotatingFileHandler(
        fn, 'midnight', atTime=now, encoding='utf-8', backupCount=1),
    logging.handlers.TimedRotatingFileHandler(
        fn, 'midnight', atTime=now, encoding='utf-8', backupCount=1),
    logging.handlers.TimedRotatingFileHandler(
        fn, 'midnight', atTime=now, encoding='utf-8', backupCount=1),
]

r = logging.makeLogRecord({'msg': 'test msg'})

handlers[0].emit(r)