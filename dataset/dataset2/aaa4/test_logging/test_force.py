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

def test_force():
    old_string_io = io.StringIO()
    new_string_io = io.StringIO()
    old_handlers = [logging.StreamHandler(old_string_io)]
    new_handlers = [logging.StreamHandler(new_string_io)]
    logging.basicConfig(level=logging.WARNING, handlers=old_handlers)
    logging.warning('warn')
    logging.info('info')
    logging.debug('debug')
    BasicConfigTest.assertEqual(len(logging.root.handlers), 1)
    logging.basicConfig(level=logging.INFO, handlers=new_handlers, force=True)
    logging.warning('warn')
    logging.info('info')
    logging.debug('debug')
    BasicConfigTest.assertEqual(len(logging.root.handlers), 1)
    BasicConfigTest.assertEqual(old_string_io.getvalue().strip(), 'WARNING:root:warn')
    BasicConfigTest.assertEqual(new_string_io.getvalue().strip(), 'WARNING:root:warn\nINFO:root:info')

BasicConfigTest = test_logging.BasicConfigTest()
test_force()
