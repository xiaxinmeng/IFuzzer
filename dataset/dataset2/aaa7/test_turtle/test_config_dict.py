import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_config_dict():
    cfg_name = TurtleConfigTest.get_cfg_file(test_config)
    parsed_cfg = turtle.config_dict(cfg_name)
    expected = {'width': 0.75, 'height': 0.8, 'canvwidth': 500, 'canvheight': 200, 'leftright': 100, 'topbottom': 100, 'mode': 'world', 'colormode': 255, 'delay': 100, 'undobuffersize': 10000, 'shape': 'circle', 'pencolor': 'red', 'fillcolor': 'blue', 'resizemode': 'auto', 'visible': None, 'language': 'english', 'exampleturtle': 'turtle', 'examplescreen': 'screen', 'title': 'Python Turtle Graphics', 'using_IDLE': ''}
    TurtleConfigTest.assertEqual(parsed_cfg, expected)

TurtleConfigTest = test_turtle.TurtleConfigTest()
test_config_dict()
