import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_partial_config_dict_with_comments():
    cfg_name = TurtleConfigTest.get_cfg_file(test_config_two)
    parsed_cfg = turtle.config_dict(cfg_name)
    expected = {'pencolor': 'red', 'fillcolor': 'blue', 'visible': False, 'language': 'english', 'using_IDLE': False}
    TurtleConfigTest.assertEqual(parsed_cfg, expected)

TurtleConfigTest = test_turtle.TurtleConfigTest()
test_partial_config_dict_with_comments()
