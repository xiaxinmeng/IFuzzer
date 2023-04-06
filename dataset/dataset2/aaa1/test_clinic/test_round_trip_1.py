from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_round_trip_1():
    ClinicBlockParserTest.round_trip('\n    verbatim text here\n    lah dee dah\n')

ClinicBlockParserTest = test_clinic.ClinicBlockParserTest()
test_round_trip_1()
