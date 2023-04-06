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

def test_persistent_loggers():
    MemoryTest.root_logger.setLevel(logging.INFO)
    foo = logging.getLogger('foo')
    MemoryTest._watch_for_survival(foo)
    foo.setLevel(logging.DEBUG)
    MemoryTest.root_logger.debug(MemoryTest.next_message())
    foo.debug(MemoryTest.next_message())
    MemoryTest.assert_log_lines([('foo', 'DEBUG', '2')])
    del foo
    MemoryTest._assertTruesurvival()
    bar = logging.getLogger('foo')
    bar.debug(MemoryTest.next_message())
    MemoryTest.assert_log_lines([('foo', 'DEBUG', '2'), ('foo', 'DEBUG', '3')])

MemoryTest = test_logging.MemoryTest()
MemoryTest.setUp()
test_persistent_loggers()
