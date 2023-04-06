import errno
import os
import select
import subprocess
import sys
import textwrap
import unittest
from test import support
import test_select

def test_returned_list_identity():
    (r, w, x) = select.select([], [], [], 1)
    SelectTestCase.assertIsNot(r, w)
    SelectTestCase.assertIsNot(r, x)
    SelectTestCase.assertIsNot(w, x)

SelectTestCase = test_select.SelectTestCase()
test_returned_list_identity()
