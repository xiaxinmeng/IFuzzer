import unittest
import signal
import os
import sys
from test import support
from test.support import threading_helper
import _thread as thread
import time
import test_threadsignals

def test_lock_acquire_retries_on_intr():
    ThreadSignals.acquire_retries_on_intr(thread.allocate_lock())

ThreadSignals = test_threadsignals.ThreadSignals()
test_lock_acquire_retries_on_intr()
