from setuptools import setup
import re

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except Exception as ex:
    with open('sasync.egg-info\requires.txt') as f:
        requirements = f.read().splitlines()

version = '0.0.1'

if not version:
    raise RuntimeError('version is not set')

with open('README') as f:
    readme = f.read()