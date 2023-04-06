import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_showturtle_hideturtle_and_isvisible():
    tpen = turtle.TPen()
    TestTPen.assertTrue(tpen.isvisible())
    tpen.hideturtle()
    TestTPen.assertFalse(tpen.isvisible())
    tpen.showturtle()
    TestTPen.assertTrue(tpen.isvisible())

TestTPen = test_turtle.TestTPen()
test_showturtle_hideturtle_and_isvisible()
