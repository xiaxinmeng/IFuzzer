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

def test_synthesize():
    webbrowser = import_helper.import_fresh_module('webbrowser')
    name = os.path.basename(sys.executable).lower()
    webbrowser.register(name, None, webbrowser.GenericBrowser(name))
    webbrowser.get(sys.executable)

ImportTest = test_webbrowser.ImportTest()
test_synthesize()
