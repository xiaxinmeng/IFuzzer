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

def test_caching():
    root = LoggerTest.root_logger
    logger1 = logging.getLogger('abc')
    logger2 = logging.getLogger('abc.def')
    root.setLevel(logging.ERROR)
    LoggerTest.assertEqual(logger2.getEffectiveLevel(), logging.ERROR)
    LoggerTest.assertEqual(logger2._cache, {})
    LoggerTest.assertTrue(logger2.isEnabledFor(logging.ERROR))
    LoggerTest.assertFalse(logger2.isEnabledFor(logging.DEBUG))
    LoggerTest.assertEqual(logger2._cache, {logging.ERROR: True, logging.DEBUG: False})
    LoggerTest.assertEqual(root._cache, {})
    LoggerTest.assertTrue(logger2.isEnabledFor(logging.ERROR))
    LoggerTest.assertEqual(root._cache, {})
    LoggerTest.assertTrue(root.isEnabledFor(logging.ERROR))
    LoggerTest.assertEqual(root._cache, {logging.ERROR: True})
    logger1.setLevel(logging.CRITICAL)
    LoggerTest.assertEqual(logger2.getEffectiveLevel(), logging.CRITICAL)
    LoggerTest.assertEqual(logger2._cache, {})
    LoggerTest.assertFalse(logger2.isEnabledFor(logging.ERROR))
    logger2.setLevel(logging.NOTSET)
    LoggerTest.assertEqual(logger2.getEffectiveLevel(), logging.CRITICAL)
    LoggerTest.assertEqual(logger2._cache, {})
    LoggerTest.assertEqual(logger1._cache, {})
    LoggerTest.assertEqual(root._cache, {})
    LoggerTest.assertFalse(logger2.isEnabledFor(logging.ERROR))
    LoggerTest.assertTrue(logger2.isEnabledFor(logging.CRITICAL))
    LoggerTest.assertFalse(logger1.isEnabledFor(logging.ERROR))
    LoggerTest.assertTrue(logger1.isEnabledFor(logging.CRITICAL))
    LoggerTest.assertTrue(root.isEnabledFor(logging.ERROR))
    logging.disable()
    LoggerTest.assertEqual(logger2.getEffectiveLevel(), logging.CRITICAL)
    LoggerTest.assertEqual(logger2._cache, {})
    LoggerTest.assertEqual(logger1._cache, {})
    LoggerTest.assertEqual(root._cache, {})
    LoggerTest.assertFalse(logger1.isEnabledFor(logging.CRITICAL))
    LoggerTest.assertFalse(logger2.isEnabledFor(logging.CRITICAL))
    LoggerTest.assertFalse(root.isEnabledFor(logging.CRITICAL))

LoggerTest = test_logging.LoggerTest()
LoggerTest.setUp()
test_caching()
