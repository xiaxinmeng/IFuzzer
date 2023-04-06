rfh = RotatingFileHandler("testing.log", delay=True)
logging.getLogger().addHandler(rfh)
logging.warning("Boo!")