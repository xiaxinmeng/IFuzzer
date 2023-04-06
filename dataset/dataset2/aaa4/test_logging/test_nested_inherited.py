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

def test_nested_inherited():
    m = BuiltinLevelsTest.next_message
    INF = logging.getLogger('INF')
    INF.setLevel(logging.INFO)
    INF_ERR = logging.getLogger('INF.ERR')
    INF_ERR.setLevel(logging.ERROR)
    INF_UNDEF = logging.getLogger('INF.UNDEF')
    INF_ERR_UNDEF = logging.getLogger('INF.ERR.UNDEF')
    UNDEF = logging.getLogger('UNDEF')
    INF_UNDEF.log(logging.CRITICAL, m())
    INF_UNDEF.error(m())
    INF_UNDEF.warning(m())
    INF_UNDEF.info(m())
    INF_ERR_UNDEF.log(logging.CRITICAL, m())
    INF_ERR_UNDEF.error(m())
    INF_UNDEF.debug(m())
    INF_ERR_UNDEF.warning(m())
    INF_ERR_UNDEF.info(m())
    INF_ERR_UNDEF.debug(m())
    BuiltinLevelsTest.assert_log_lines([('INF.UNDEF', 'CRITICAL', '1'), ('INF.UNDEF', 'ERROR', '2'), ('INF.UNDEF', 'WARNING', '3'), ('INF.UNDEF', 'INFO', '4'), ('INF.ERR.UNDEF', 'CRITICAL', '5'), ('INF.ERR.UNDEF', 'ERROR', '6')])

BuiltinLevelsTest = test_logging.BuiltinLevelsTest()
BuiltinLevelsTest.setUp()
test_nested_inherited()
