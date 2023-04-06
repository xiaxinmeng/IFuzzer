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

@unittest.skipUnless(hasattr(logging.handlers, 'QueueListener'), 'logging.handlers.QueueListener required for this test')
def test_queue_listener():
    handler = TestHandler(support.Matcher())
    listener = logging.handlers.QueueListener(QueueHandlerTest.queue, handler)
    listener.start()
    try:
        QueueHandlerTest.que_logger.warning(QueueHandlerTest.next_message())
        QueueHandlerTest.que_logger.error(QueueHandlerTest.next_message())
        QueueHandlerTest.que_logger.critical(QueueHandlerTest.next_message())
    finally:
        listener.stop()
    QueueHandlerTest.assertTrue(handler.matches(levelno=logging.WARNING, message='1'))
    QueueHandlerTest.assertTrue(handler.matches(levelno=logging.ERROR, message='2'))
    QueueHandlerTest.assertTrue(handler.matches(levelno=logging.CRITICAL, message='3'))
    handler.close()
    handler = TestHandler(support.Matcher())
    handler.setLevel(logging.CRITICAL)
    listener = logging.handlers.QueueListener(QueueHandlerTest.queue, handler, respect_handler_level=True)
    listener.start()
    try:
        QueueHandlerTest.que_logger.warning(QueueHandlerTest.next_message())
        QueueHandlerTest.que_logger.error(QueueHandlerTest.next_message())
        QueueHandlerTest.que_logger.critical(QueueHandlerTest.next_message())
    finally:
        listener.stop()
    QueueHandlerTest.assertFalse(handler.matches(levelno=logging.WARNING, message='4'))
    QueueHandlerTest.assertFalse(handler.matches(levelno=logging.ERROR, message='5'))
    QueueHandlerTest.assertTrue(handler.matches(levelno=logging.CRITICAL, message='6'))
    handler.close()

QueueHandlerTest = test_logging.QueueHandlerTest()
QueueHandlerTest.setUp()
test_queue_listener()
