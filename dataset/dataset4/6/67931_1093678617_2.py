from distutils.core import setup
from distutils.extension import Extension
import Cython.Compiler.Options
from Cython.Distutils import build_ext
from os.path import join, sep, dirname, abspath

def get_extensions_from_sources():
    ext_modules = []
    ext_modules.append(Extension('src.cplayground', sources=['src/cplayground.c']))
    ext_modules.append(Extension('src.cppplayground', sources=['src/cplayground.cpp']))
    return ext_modules