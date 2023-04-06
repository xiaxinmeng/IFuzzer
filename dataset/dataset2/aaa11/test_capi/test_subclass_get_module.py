from collections import OrderedDict
import os
import pickle
import random
import re
import subprocess
import sys
import textwrap
import threading
import time
import unittest
import weakref
import importlib.machinery
import importlib.util
from test import support
from test.support import MISSING_C_DOCSTRINGS
from test.support import import_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_failure, assert_python_ok
import _posixsubprocess
import _testinternalcapi
from _testcapi import MyList
from _testcapi import MyList
from _testcapi import pynumber_tobase
import builtins
import binascii
import test_capi

def test_subclass_get_module():
    """PyType_GetModule for defining_class"""

    class StateAccessType_Subclass(Test_ModuleStateAccess.module.StateAccessType):
        pass
    instance = StateAccessType_Subclass()
    Test_ModuleStateAccess.assertIs(instance.get_defining_module(), Test_ModuleStateAccess.module)

Test_ModuleStateAccess = test_capi.Test_ModuleStateAccess()
Test_ModuleStateAccess.setUp()
test_subclass_get_module()
