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

def test_rollover_filenames():

    def namer(name):
        return name + '.test'
    rh = logging.handlers.RotatingFileHandler(RotatingFileHandlerTest.fn, backupCount=2, maxBytes=1)
    rh.namer = namer
    rh.emit(RotatingFileHandlerTest.next_rec())
    RotatingFileHandlerTest.assertLogFile(RotatingFileHandlerTest.fn)
    rh.emit(RotatingFileHandlerTest.next_rec())
    RotatingFileHandlerTest.assertLogFile(namer(RotatingFileHandlerTest.fn + '.1'))
    rh.emit(RotatingFileHandlerTest.next_rec())
    RotatingFileHandlerTest.assertLogFile(namer(RotatingFileHandlerTest.fn + '.2'))
    RotatingFileHandlerTest.assertFalse(os.path.exists(namer(RotatingFileHandlerTest.fn + '.3')))
    rh.close()

RotatingFileHandlerTest = test_logging.RotatingFileHandlerTest()
RotatingFileHandlerTest .setUp()
test_rollover_filenames()
