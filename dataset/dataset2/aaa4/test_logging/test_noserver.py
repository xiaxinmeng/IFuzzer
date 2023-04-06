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

def test_noserver():
    if SocketHandlerTest.server_exception:
        SocketHandlerTest.skipTest(SocketHandlerTest.server_exception)
    SocketHandlerTest.sock_hdlr.retryStart = 2.5
    SocketHandlerTest.server.stop()
    try:
        raise RuntimeError('Deliberate mistake')
    except RuntimeError:
        SocketHandlerTest.root_logger.exception('Never sent')
    SocketHandlerTest.root_logger.error('Never sent, either')
    now = time.time()
    SocketHandlerTest.assertGreater(SocketHandlerTest.sock_hdlr.retryTime, now)
    time.sleep(SocketHandlerTest.sock_hdlr.retryTime - now + 0.001)
    SocketHandlerTest.root_logger.error('Nor this')

SocketHandlerTest = test_logging.SocketHandlerTest()
SocketHandlerTest.setUp()
test_noserver()
