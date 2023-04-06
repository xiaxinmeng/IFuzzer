logging.addHandler(StreamHandler(level=ERROR))
logging.addHandler(RotatingFileHandler("mylog",level=DEBUG))