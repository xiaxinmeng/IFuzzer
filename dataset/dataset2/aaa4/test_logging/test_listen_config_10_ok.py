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

def test_listen_config_10_ok():
    with support.captured_stdout() as output:
        ConfigDictTest.setup_via_listener(json.dumps(ConfigDictTest.config10))
        logger = logging.getLogger('compiler.parser')
        logger.warning(ConfigDictTest.next_message())
        logger = logging.getLogger('compiler')
        logger.warning(ConfigDictTest.next_message())
        logger = logging.getLogger('compiler.lexer')
        logger.warning(ConfigDictTest.next_message())
        logger = logging.getLogger('compiler.parser.codegen')
        logger.error(ConfigDictTest.next_message())
        ConfigDictTest.assert_log_lines([('WARNING', '1'), ('ERROR', '4')], stream=output)

ConfigDictTest = test_logging.ConfigDictTest()
test_listen_config_10_ok()
