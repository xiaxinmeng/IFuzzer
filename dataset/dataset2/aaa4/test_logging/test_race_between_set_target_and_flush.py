import logging
import logging.handlers
import logging.config
import codecs
import configparser
import copy
import datetime
import pathlib
import pickle
import io
import gc
import json
import os
import queue
import random
import re
import socket
import struct
import sys
import tempfile
from test.support.script_helper import assert_python_ok, assert_python_failure
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.logging_helper import TestHandler
import textwrap
import threading
import time
import unittest
import warnings
import weakref
import asyncore
from http.server import HTTPServer, BaseHTTPRequestHandler
import smtpd
from urllib.parse import urlparse, parse_qs
from socketserver import ThreadingUDPServer, DatagramRequestHandler, ThreadingTCPServer, StreamRequestHandler

import zlib
import ssl
from collections import namedtuple
import multiprocessing
from unittest.mock import patch
import multiprocessing as mp
import multiprocessing
import multiprocessing
import test_logging

def test_race_between_set_target_and_flush():

    class MockRaceConditionHandler:

        def __init__(MemoryHandlerTest, mem_hdlr):
            MemoryHandlerTest.mem_hdlr = mem_hdlr
            MemoryHandlerTest.threads = []

        def removeTarget(MemoryHandlerTest):
            MemoryHandlerTest.mem_hdlr.setTarget(None)

        def handle(MemoryHandlerTest, msg):
            thread = threading.Thread(target=MemoryHandlerTest.removeTarget)
            MemoryHandlerTest.threads.append(thread)
            thread.start()
    target = MockRaceConditionHandler(MemoryHandlerTest.mem_hdlr)
    try:
        MemoryHandlerTest.mem_hdlr.setTarget(target)
        for _ in range(10):
            time.sleep(0.005)
            MemoryHandlerTest.mem_logger.info('not flushed')
            MemoryHandlerTest.mem_logger.warning('flushed')
    finally:
        for thread in target.threads:
            threading_helper.join_thread(thread)

MemoryHandlerTest = test_logging.MemoryHandlerTest()
MemoryHandlerTest.setUp()
test_race_between_set_target_and_flush()
