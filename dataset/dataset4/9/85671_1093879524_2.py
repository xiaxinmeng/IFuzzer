
import os
import logging

import CONSTANTS


class LogFile:
    def __init__(self, logger_name):
        if not os.path.exists(CONSTANTS.PROCESS_DATA_DIR):
            os.makedirs(CONSTANTS.PROCESS_DATA_DIR)

        self.path = f'{CONSTANTS.PROCESS_DATA_DIR}/{logger_name}.log'
        self.file_handler = logging.FileHandler(self.path)

        self.logger = logging.getLogger(f'{logger_name}')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.file_handler)

    def entry(self, text):
        self.logger.info(text)


EXCIPIENTS = LogFile('excipients')

