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

def test_encoding_errors():
    try:
        encoding = 'ascii'
        logging.basicConfig(filename='test.log', encoding=encoding, errors='ignore', format='%(message)s', level=logging.DEBUG)
        BasicConfigTest.assertEqual(len(logging.root.handlers), 1)
        handler = logging.root.handlers[0]
        BasicConfigTest.assertIsInstance(handler, logging.FileHandler)
        BasicConfigTest.assertEqual(handler.encoding, encoding)
        logging.debug('The Øresund Bridge joins Copenhagen to Malmö')
    finally:
        handler.close()
        with open('test.log', encoding='utf-8') as f:
            data = f.read().strip()
        os.remove('test.log')
        BasicConfigTest.assertEqual(data, 'The resund Bridge joins Copenhagen to Malm')

BasicConfigTest = test_logging.BasicConfigTest()
test_encoding_errors()