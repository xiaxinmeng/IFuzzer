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

def test_exception_excinfo():
    try:
        1 / 0
    except ZeroDivisionError as e:
        exc = e
    LoggerAdapterTest.adapter.exception('exc_info test', exc_info=exc)
    LoggerAdapterTest.assertEqual(len(LoggerAdapterTest.recording.records), 1)
    record = LoggerAdapterTest.recording.records[0]
    LoggerAdapterTest.assertEqual(record.exc_info, (exc.__class__, exc, exc.__traceback__))

LoggerAdapterTest = test_logging.LoggerAdapterTest()
LoggerAdapterTest.setUp()
test_exception_excinfo()
