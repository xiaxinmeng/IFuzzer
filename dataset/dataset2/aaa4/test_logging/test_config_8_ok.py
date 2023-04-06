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

def test_config_8_ok():
    with support.captured_stdout() as output:
        ConfigDictTest.apply_config(ConfigDictTest.config1)
        logger = logging.getLogger('compiler.parser')
        logger.info(ConfigDictTest.next_message())
        logger.error(ConfigDictTest.next_message())
        ConfigDictTest.assert_log_lines([('INFO', '1'), ('ERROR', '2')], stream=output)
        ConfigDictTest.assert_log_lines([])
    with support.captured_stdout() as output:
        ConfigDictTest.apply_config(ConfigDictTest.config8)
        logger = logging.getLogger('compiler.parser')
        ConfigDictTest.assertFalse(logger.disabled)
        logger.info(ConfigDictTest.next_message())
        logger.error(ConfigDictTest.next_message())
        logger = logging.getLogger('compiler.lexer')
        logger.info(ConfigDictTest.next_message())
        logger.error(ConfigDictTest.next_message())
        ConfigDictTest.assert_log_lines([('INFO', '3'), ('ERROR', '4'), ('INFO', '5'), ('ERROR', '6')], stream=output)
        ConfigDictTest.assert_log_lines([])

ConfigDictTest = test_logging.ConfigDictTest()
ConfigDictTest.setUp()
test_config_8_ok()
