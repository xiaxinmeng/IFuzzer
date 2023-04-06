class CustomHandler(logging.Handler):
    def __init__(self, queue):
        logging.Handler.__init__(self)
        self.queue = queue
        
    def emit(self, record):
        try:
            ei = record.exc_info
            if ei:
                dummy = self.format(record)
                record.exc_info = None  
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)