logger = logging.getLogger(name='main')
logger.setLevel(logging.INFO)

logger1 = logging.getLogger(name='main1')
logger1.setLevel(logging.INFO)
ch = logging.StreamHandler()
logger1_formatter = logging.Formatter('logger 1 handler : %(message)s')
ch.setFormatter(logger1_formatter)
logger1.addHandler(ch)

logger.error('logger XXX') # calls root logger's handler
logging.error('root logger XXX') # calls root logger's handler
logger1.error('logger 1 XXX') # Calls ch and then root logger's handler

logger1.propagate = False
logger1.error('logger 1 XXX') # Calls only ch since propagation is set to False and root handler is not called