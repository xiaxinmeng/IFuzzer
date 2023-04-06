import sys
import os
import subprocess
from multiprocessing import Pool, Value, Queue
import multiprocessing
import logging
import logging.handlers
import pickle

queue = multiprocessing.Manager().Queue(-1)
qh = logging.handlers.QueueHandler(queue)
pickle.dumps(qh)