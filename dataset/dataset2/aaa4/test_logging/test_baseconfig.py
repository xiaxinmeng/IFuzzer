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

def test_baseconfig():
    d = {'atuple': (1, 2, 3), 'alist': ['a', 'b', 'c'], 'adict': {'d': 'e', 'f': 3}, 'nest1': ('g', ('h', 'i'), 'j'), 'nest2': ['k', ['l', 'm'], 'n'], 'nest3': ['o', 'cfg://alist', 'p']}
    bc = logging.config.BaseConfigurator(d)
    ConfigDictTest.assertEqual(bc.convert('cfg://atuple[1]'), 2)
    ConfigDictTest.assertEqual(bc.convert('cfg://alist[1]'), 'b')
    ConfigDictTest.assertEqual(bc.convert('cfg://nest1[1][0]'), 'h')
    ConfigDictTest.assertEqual(bc.convert('cfg://nest2[1][1]'), 'm')
    ConfigDictTest.assertEqual(bc.convert('cfg://adict.d'), 'e')
    ConfigDictTest.assertEqual(bc.convert('cfg://adict[f]'), 3)
    v = bc.convert('cfg://nest3')
    ConfigDictTest.assertEqual(v.pop(1), ['a', 'b', 'c'])
    ConfigDictTest.assertRaises(KeyError, bc.convert, 'cfg://nosuch')
    ConfigDictTest.assertRaises(ValueError, bc.convert, 'cfg://!')
    ConfigDictTest.assertRaises(KeyError, bc.convert, 'cfg://adict[2]')

ConfigDictTest = test_logging.ConfigDictTest()
test_baseconfig()
