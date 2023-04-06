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

def test_instance_assignment():
    cfg = configparser.ConfigParser()
    cfg.getboolean = lambda section, option: True
    cfg.getlen = lambda section, option: len(cfg[section][option])
    cfg.read_string(BlatantOverrideConvertersTestCase.config)
    BlatantOverrideConvertersTestCase.assertEqual(len(cfg.converters), 3)
    BlatantOverrideConvertersTestCase.assertIn('boolean', cfg.converters)
    BlatantOverrideConvertersTestCase.assertNotIn('len', cfg.converters)
    BlatantOverrideConvertersTestCase.assertIsNone(cfg.converters['int'])
    BlatantOverrideConvertersTestCase.assertIsNone(cfg.converters['float'])
    BlatantOverrideConvertersTestCase.assertIsNone(cfg.converters['boolean'])
    BlatantOverrideConvertersTestCase.assertTrue(cfg.getboolean('one', 'one'))
    BlatantOverrideConvertersTestCase.assertTrue(cfg.getboolean('two', 'two'))
    BlatantOverrideConvertersTestCase.assertTrue(cfg.getboolean('one', 'two'))
    BlatantOverrideConvertersTestCase.assertTrue(cfg.getboolean('two', 'one'))
    cfg.converters['boolean'] = cfg._convert_to_boolean
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('one', 'one'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('two', 'two'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('one', 'two'))
    BlatantOverrideConvertersTestCase.assertFalse(cfg.getboolean('two', 'one'))
    BlatantOverrideConvertersTestCase.assertEqual(cfg.getlen('one', 'one'), 5)
    BlatantOverrideConvertersTestCase.assertEqual(cfg.getlen('one', 'two'), 5)
    BlatantOverrideConvertersTestCase.assertEqual(cfg.getlen('one', 'three'), 16)
    BlatantOverrideConvertersTestCase.assertEqual(cfg.getlen('two', 'one'), 5)
    BlatantOverrideConvertersTestCase.assertEqual(cfg.getlen('two', 'two'), 5)
    BlatantOverrideConvertersTestCase.assertEqual(cfg.getlen('two', 'three'), 4)
    with BlatantOverrideConvertersTestCase.assertRaises(AttributeError):
        BlatantOverrideConvertersTestCase.assertEqual(cfg['one'].getlen('one'), 5)
    with BlatantOverrideConvertersTestCase.assertRaises(AttributeError):
        BlatantOverrideConvertersTestCase.assertEqual(cfg['two'].getlen('one'), 5)

BlatantOverrideConvertersTestCase = test_configparser.BlatantOverrideConvertersTestCase()
test_instance_assignment()
