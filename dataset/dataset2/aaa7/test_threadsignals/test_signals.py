import unittest
import signal
import os
import sys
from test import support
from test.support import threading_helper
import _thread as thread
import time
import test_threadsignals

def test_signals():
    with threading_helper.wait_threads_exit():
        test_threadsignals.signalled_all.acquire()
        ThreadSignals.spawnSignallingThread()
        signalled_all.acquire()
    if signal_blackboard[signal.SIGUSR1]['tripped'] == 0 or signal_blackboard[signal.SIGUSR2]['tripped'] == 0:
        try:
            signal.alarm(1)
            signal.pause()
        finally:
            signal.alarm(0)
    ThreadSignals.assertEqual(signal_blackboard[signal.SIGUSR1]['tripped'], 1)
    ThreadSignals.assertEqual(signal_blackboard[signal.SIGUSR1]['tripped_by'], thread.get_ident())
    ThreadSignals.assertEqual(signal_blackboard[signal.SIGUSR2]['tripped'], 1)
    ThreadSignals.assertEqual(signal_blackboard[signal.SIGUSR2]['tripped_by'], thread.get_ident())
    signalled_all.release()

ThreadSignals = test_threadsignals.ThreadSignals()
test_signals()
