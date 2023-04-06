from types import ModuleType
from importlib.machinery import ModuleSpec, SourceFileLoader
from _frozen_importlib import _SpecMethods

loader = SourceFileLoader('plugin_base', 'my_file.py')
spec = ModuleSpec(name=loader.name, loader=loader)
mod = _SpecMethods(spec).create()