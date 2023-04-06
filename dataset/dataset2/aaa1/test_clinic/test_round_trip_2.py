from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_round_trip_2():
    ClinicBlockParserTest.round_trip('\n    verbatim text here\n    lah dee dah\n/*[inert]\nabc\n[inert]*/\ndef\n/*[inert checksum: 7b18d017f89f61cf17d47f92749ea6930a3f1deb]*/\nxyz\n')

ClinicBlockParserTest = test_clinic.ClinicBlockParserTest()
test_round_trip_2()
