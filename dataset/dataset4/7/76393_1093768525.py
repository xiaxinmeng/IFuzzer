logger = logging.getLogger(name)
logger.setLevel(level=logging.DEBUG)
...
stream_handler = logging.StreamHandler(stream=stdout)
stream_handler.setLevel(logging_level)
stream_handler.setFormatter(fmt=formatter)