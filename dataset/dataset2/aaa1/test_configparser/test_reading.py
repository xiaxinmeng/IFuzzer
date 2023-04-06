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

def test_reading():
    smbconf = support.findfile('cfgparser.2')
    cf = RawConfigParserTestSambaConf.newconfig()
    parsed_files = cf.read([smbconf, 'nonexistent-file'], encoding='utf-8')
    RawConfigParserTestSambaConf.assertEqual(parsed_files, [smbconf])
    sections = ['global', 'homes', 'printers', 'print$', 'pdf-generator', 'tmp', 'Agustin']
    RawConfigParserTestSambaConf.assertEqual(cf.sections(), sections)
    RawConfigParserTestSambaConf.assertEqual(cf.get('global', 'workgroup'), 'MDKGROUP')
    RawConfigParserTestSambaConf.assertEqual(cf.getint('global', 'max log size'), 50)
    RawConfigParserTestSambaConf.assertEqual(cf.get('global', 'hosts allow'), '127.')
    RawConfigParserTestSambaConf.assertEqual(cf.get('tmp', 'echo command'), 'cat %s; rm %s')

RawConfigParserTestSambaConf = test_configparser.RawConfigParserTestSambaConf()
test_reading()
