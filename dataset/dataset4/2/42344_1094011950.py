import logging
import logging.handlers

if __name__ == "__main__":
    fh = logging.handlers.RotatingFileHandler("log.txt")
    mh = logging.handlers.MemoryHandler(1024, 
logging.ERROR, fh)
    logging.getLogger().addHandler(mh)
    logging.getLogger().warning("next statement crashes")
    logging.shutdown()