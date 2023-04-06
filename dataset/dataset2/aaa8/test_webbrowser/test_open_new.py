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

def test_open_new():
    ChromeCommandTest._test('open_new', options=['-remote'], arguments=['openURL({},new-window)'.format(test_webbrowser.URL)])

ChromeCommandTest = test_webbrowser.ChromeCommandTest()
ChromeCommandTest.setUp()
test_open_new()
