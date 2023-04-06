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

def test_inheritance():

    class StrangeConfigParser(configparser.ConfigParser):
        gettysburg = 'a historic borough in south central Pennsylvania'

        def getboolean(BlatantOverrideConvertersTestCase, section, option, *, raw=False, vars=None, fallback=configparser._UNSET):
            if section == option:
                return True
            return super().getboolean(section, option, raw=raw, vars=vars, fallback=fallback)

        def getlen(BlatantOverrideConvertersTestCase, section, option, *, raw=False, vars=None, fallback=configparser._UNSET):
            return BlatantOverrideConvertersTestCase._get_conv(section, option, len, raw=raw, vars=vars, fallback=fallback)
    cfg = StrangeConfigParser()
    cfg.read_string(BlatantOverrideConvertersTestCase.config)
    BlatantOverrideConvertersTestCase._test_len(cfg)
    BlatantOverrideConvertersTestCase.assertIsNone(cfg.converters['len'])
    BlatantOverrideConvertersTestCase.assertTrue(cfg.getboolean('one', 'one'))
    BlatantOverrideConvertersTestCase.assertTrue(cfg.getboolean('two', 'two'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('one', 'two'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('two', 'one'))
    cfg.converters['boolean'] = cfg._convert_to_boolean
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('one', 'one'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('two', 'two'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('one', 'two'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('two', 'one'))

BlatantOverrideConvertersTestCase = test_configparser.BlatantOverrideConvertersTestCase()
test_inheritance()
