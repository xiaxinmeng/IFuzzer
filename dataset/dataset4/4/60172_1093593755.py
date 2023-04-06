from test import support; support.use_resources = ['gui']
import unittest
unittest.main('test.test_tcl', exit=False)
unittest.main('test.test_idle', exit=False)