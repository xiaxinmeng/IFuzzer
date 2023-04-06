
from distutils.core import Extension, setup

extension = Extension("breaky", ["breaky.c"])

setup(
    name="tp_clear",
    version="0.1.0",
    ext_modules=[extension],
)
