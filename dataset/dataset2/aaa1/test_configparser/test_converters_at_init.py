import collections
import configparser
import io
import os
import pathlib
import textwrap
import unittest
import warnings
from test import support
from test.support import os_helper
import decimal
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import decimal
import test_configparser

def test_converters_at_init():
    cfg = configparser.ConfigParser(converters={'len': len})
    cfg.read_string(BlatantOverrideConvertersTestCase.config)
    BlatantOverrideConvertersTestCase._test_len(cfg)
    BlatantOverrideConvertersTestCase.assertIsNotNone(cfg.converters['len'])

BlatantOverrideConvertersTestCase = test_configparser.BlatantOverrideConvertersTestCase()
test_converters_at_init()
