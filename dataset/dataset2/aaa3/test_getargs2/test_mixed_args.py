import unittest
import math
import string
import sys
from test import support
from test.support import import_helper
from _testcapi import getargs_keywords, getargs_keyword_only
from _testcapi import UCHAR_MAX, USHRT_MAX, UINT_MAX, ULONG_MAX, INT_MAX, INT_MIN, LONG_MIN, LONG_MAX, PY_SSIZE_T_MIN, PY_SSIZE_T_MAX, SHRT_MIN, SHRT_MAX, FLT_MIN, FLT_MAX, DBL_MIN, DBL_MAX
from _testcapi import getargs_b
from _testcapi import getargs_B
from _testcapi import getargs_H
from _testcapi import getargs_I
from _testcapi import getargs_k
from _testcapi import getargs_h
from _testcapi import getargs_i
from _testcapi import getargs_l
from _testcapi import getargs_n
from _testcapi import getargs_L
from _testcapi import getargs_K
from _testcapi import getargs_f
from _testcapi import getargs_f
from _testcapi import getargs_d
from _testcapi import getargs_D
from _testcapi import getargs_p
from _testcapi import get_args
from _testcapi import getargs_tuple
from _testcapi import get_kwargs
from _testcapi import getargs_positional_only_and_keywords as getargs
from _testcapi import getargs_c
from _testcapi import getargs_y
from _testcapi import getargs_y_star
from _testcapi import getargs_y_hash
from _testcapi import getargs_w_star
from _testcapi import getargs_C
from _testcapi import getargs_s
from _testcapi import getargs_s_star
from _testcapi import getargs_s_hash
from _testcapi import getargs_z
from _testcapi import getargs_z_star
from _testcapi import getargs_z_hash
from _testcapi import getargs_es
from _testcapi import getargs_et
from _testcapi import getargs_es_hash
from _testcapi import getargs_et_hash
from _testcapi import getargs_u
from _testcapi import getargs_u_hash
from _testcapi import getargs_Z
from _testcapi import getargs_Z_hash
from _testcapi import getargs_S
from _testcapi import getargs_Y
from _testcapi import getargs_U
import test_getargs2

def test_mixed_args():
    Keywords_TestCase.assertEqual(Keywords_TestCase.getargs(1, 2, keyword=3), (1, 2, 3))

Keywords_TestCase = test_getargs2.Keywords_TestCase()
Keywords_TestCase.setUp()
test_mixed_args()
