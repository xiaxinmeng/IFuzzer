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

def test_register():
    webbrowser = import_helper.import_fresh_module('webbrowser')
    BrowserRegistrationTest.assertIsNone(webbrowser._tryorder)
    BrowserRegistrationTest.assertFalse(webbrowser._browsers)

    class ExampleBrowser:
        pass
    webbrowser.register('Example1', ExampleBrowser)
    BrowserRegistrationTest.assertTrue(webbrowser._tryorder)
    BrowserRegistrationTest.assertEqual(webbrowser._tryorder[-1], 'Example1')
    BrowserRegistrationTest.assertTrue(webbrowser._browsers)
    BrowserRegistrationTest.assertIn('example1', webbrowser._browsers)
    BrowserRegistrationTest.assertEqual(webbrowser._browsers['example1'], [ExampleBrowser, None])

BrowserRegistrationTest = test_webbrowser.BrowserRegistrationTest()
test_register()
