import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_ip_address():
    FactoryFunctionErrors.assertFactoryError(ipaddress.ip_address, 'address')

FactoryFunctionErrors = test_ipaddress.FactoryFunctionErrors()
test_ip_address()
