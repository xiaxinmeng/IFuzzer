#!/usr/bin/env python
from lib2to3 import refactor
import sys
import os

fixers = os.path.join(os.path.dirname(refactor.__file__), "fixes")
sys.exit(refactor.main(fixers))