import logging
import os
import sys
import threading

def lockie():
    while True:
        # this adds handle to _at_fork_acquire_release_weakset
        #sys.stdout.write(".")
        #sys.stdout.flush()
        h = logging.Handler()