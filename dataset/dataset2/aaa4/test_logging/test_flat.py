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

def test_flat():
    m = BuiltinLevelsTest.next_message
    ERR = logging.getLogger('ERR')
    ERR.setLevel(logging.ERROR)
    INF = logging.LoggerAdapter(logging.getLogger('INF'), {})
    INF.setLevel(logging.INFO)
    DEB = logging.getLogger('DEB')
    DEB.setLevel(logging.DEBUG)
    ERR.log(logging.CRITICAL, m())
    ERR.error(m())
    INF.log(logging.CRITICAL, m())
    INF.error(m())
    INF.warning(m())
    INF.info(m())
    DEB.log(logging.CRITICAL, m())
    DEB.error(m())
    DEB.warning(m())
    DEB.info(m())
    DEB.debug(m())
    ERR.warning(m())
    ERR.info(m())
    ERR.debug(m())
    INF.debug(m())
    BuiltinLevelsTest.assert_log_lines([('ERR', 'CRITICAL', '1'), ('ERR', 'ERROR', '2'), ('INF', 'CRITICAL', '3'), ('INF', 'ERROR', '4'), ('INF', 'WARNING', '5'), ('INF', 'INFO', '6'), ('DEB', 'CRITICAL', '7'), ('DEB', 'ERROR', '8'), ('DEB', 'WARNING', '9'), ('DEB', 'INFO', '10'), ('DEB', 'DEBUG', '11')])

BuiltinLevelsTest = test_logging.BuiltinLevelsTest()
BuiltinLevelsTest.setUp()
test_flat()
