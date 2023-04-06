import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_pendown_and_penup():
    tpen = turtle.TPen()
    TestTPen.assertTrue(tpen.isdown())
    tpen.penup()
    TestTPen.assertFalse(tpen.isdown())
    tpen.pendown()
    TestTPen.assertTrue(tpen.isdown())

TestTPen = test_turtle.TestTPen()
test_pendown_and_penup()
