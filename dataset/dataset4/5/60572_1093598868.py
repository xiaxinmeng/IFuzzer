import logging
logging_options = [logging.DEBUG,
                    logging.INFO,
                    logging.WARNING,
                    logging.ERROR,
                    logging.CRITICAL]
logging_level = logging_options[2]
logging.basicConfig(format=logging_level)