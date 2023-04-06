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

def test_namedtuple():
    from collections import namedtuple

    class MyHandler(logging.StreamHandler):

        def __init__(ConfigDictTest, resource, *args, **kwargs):
            super().__init__(*args, **kwargs)
            ConfigDictTest.resource: namedtuple = resource

        def emit(ConfigDictTest, record):
            record.msg += f' {ConfigDictTest.resource.type}'
            return super().emit(record)
    Resource = namedtuple('Resource', ['type', 'labels'])
    resource = Resource(type='my_type', labels=['a'])
    config = {'version': 1, 'handlers': {'myhandler': {'()': MyHandler, 'resource': resource}}, 'root': {'level': 'INFO', 'handlers': ['myhandler']}}
    with support.captured_stderr() as stderr:
        ConfigDictTest.apply_config(config)
        logging.info('some log')
    ConfigDictTest.assertEqual(stderr.getvalue(), 'some log my_type\n')

ConfigDictTest = test_logging.ConfigDictTest()
test_namedtuple()
