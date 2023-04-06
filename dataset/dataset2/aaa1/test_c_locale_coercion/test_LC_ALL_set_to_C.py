import locale
import os
import subprocess
import sys
import sysconfig
import unittest
from collections import namedtuple
from test import support
from test.support.script_helper import run_python_until_end
import test_c_locale_coercion

def test_LC_ALL_set_to_C():
    LocaleCoercionTests._check_c_locale_coercion(test_c_locale_coercion.EXPECTED_C_LOCALE_FS_ENCODING, test_c_locale_coercion.EXPECTED_C_LOCALE_STREAM_ENCODING, coerce_c_locale=None, LC_ALL='C', coercion_expected=False)
    LocaleCoercionTests._check_c_locale_coercion(test_c_locale_coercion.EXPECTED_C_LOCALE_FS_ENCODING, test_c_locale_coercion.EXPECTED_C_LOCALE_STREAM_ENCODING, coerce_c_locale='warn', LC_ALL='C', expected_warnings=[test_c_locale_coercion.LEGACY_LOCALE_WARNING], coercion_expected=False)

LocaleCoercionTests = test_c_locale_coercion.LocaleCoercionTests()
test_LC_ALL_set_to_C()
