log_filename = os.path.join(log_dir, "application.log")
log_handler = logging.handlers.TimedRotatingFileHandler(log_filename, when='MIDNIGHT', interval=1, backupCount=7)