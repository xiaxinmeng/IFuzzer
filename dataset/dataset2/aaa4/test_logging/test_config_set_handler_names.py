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

def test_config_set_handler_names():
    test_config = '\n            [loggers]\n            keys=root\n\n            [handlers]\n            keys=hand1\n\n            [formatters]\n            keys=form1\n\n            [logger_root]\n            handlers=hand1\n\n            [handler_hand1]\n            class=StreamHandler\n            formatter=form1\n\n            [formatter_form1]\n            format=%(levelname)s ++ %(message)s\n            '
    ConfigFileTest.apply_config(test_config)
    ConfigFileTest.assertEqual(logging.getLogger().handlers[0].name, 'hand1')

ConfigFileTest = test_logging.ConfigFileTest()
test_config_set_handler_names()
