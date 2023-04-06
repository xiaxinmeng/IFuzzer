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

def test_open_with_autoraise_false():
    ChromeCommandTest._test('open', options=['-remote'], arguments=['openURL({})'.format(test_webbrowser.URL)])

ChromeCommandTest = test_webbrowser.ChromeCommandTest()
test_open_with_autoraise_false()
