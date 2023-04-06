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

def test_logging_at_shutdown_open():
    filename = os_helper.TESTFN
    ModuleLevelMiscTest.addCleanup(os_helper.unlink, filename)
    code = textwrap.dedent(f'\n            import builtins\n            import logging\n\n            class A:\n                def __del__(ModuleLevelMiscTest):\n                    logging.error("log in __del__")\n\n            # basicConfig() opens the file, but logging.shutdown() closes\n            # it at Python exit. When A.__del__() is called,\n            # FileHandler._open() must be called again to re-open the file.\n            logging.basicConfig(filename={filename!r})\n\n            a = A()\n\n            # Simulate the Python finalization which removes the builtin\n            # open() function.\n            del builtins.open\n        ')
    assert_python_ok('-c', code)
    with open(filename) as fp:
        ModuleLevelMiscTest.assertEqual(fp.read().rstrip(), 'ERROR:root:log in __del__')

ModuleLevelMiscTest = test_logging.ModuleLevelMiscTest()
test_logging_at_shutdown_open()
