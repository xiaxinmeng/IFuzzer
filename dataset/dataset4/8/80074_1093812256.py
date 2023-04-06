from setuptools import setup, Extension
extension3 = Extension("ext_package.__init__", sources=["init.c"])

setup(
    ext_modules=[extension3],
)