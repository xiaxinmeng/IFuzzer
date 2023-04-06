import webbrowser
import unittest
import os
import sys
import subprocess
from unittest import mock
from test import support
from test.support import import_helper
from test.support import os_helper
import test_webbrowser

def test_get():
    webbrowser = import_helper.import_fresh_module('webbrowser')
    ImportTest.assertIsNone(webbrowser._tryorder)
    ImportTest.assertFalse(webbrowser._browsers)
    with ImportTest.assertRaises(webbrowser.Error):
        webbrowser.get('fakebrowser')
    ImportTest.assertIsNotNone(webbrowser._tryorder)

ImportTest = test_webbrowser.ImportTest()
test_get()
