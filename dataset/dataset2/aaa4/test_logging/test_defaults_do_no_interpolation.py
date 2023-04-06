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

def test_defaults_do_no_interpolation():
    """bpo-33802 defaults should not get interpolated"""
    ini = textwrap.dedent('\n            [formatters]\n            keys=default\n\n            [formatter_default]\n\n            [handlers]\n            keys=console\n\n            [handler_console]\n            class=logging.StreamHandler\n            args=tuple()\n\n            [loggers]\n            keys=root\n\n            [logger_root]\n            formatter=default\n            handlers=console\n            ').strip()
    (fd, fn) = tempfile.mkstemp(prefix='test_logging_', suffix='.ini')
    try:
        os.write(fd, ini.encode('ascii'))
        os.close(fd)
        logging.config.fileConfig(fn, defaults=dict(version=1, disable_existing_loggers=False, formatters={'generic': {'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s', 'datefmt': '[%Y-%m-%d %H:%M:%S %z]', 'class': 'logging.Formatter'}}))
    finally:
        os.unlink(fn)

ConfigFileTest = test_logging.ConfigFileTest()
test_defaults_do_no_interpolation()
