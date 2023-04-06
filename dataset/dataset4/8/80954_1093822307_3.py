import threading
import pickle

import logging

threads = []

def pickle_load_thread():

    logging.error("Thread %d loading", threading.get_ident())