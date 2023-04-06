
# numpy/__init__.py
import importlib.metadata as metadata

__version__ = metadata.dist_for_module('numpy', __spec__).version
