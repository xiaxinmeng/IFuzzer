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

def test_register_default():
    BrowserRegistrationTest._check_registration(preferred=None)

BrowserRegistrationTest = test_webbrowser.BrowserRegistrationTest()
test_register_default()
