
from argparse import ArgumentParser

ArgumentParser(
  prog=None if globals().get('__spec__') is None else 'python -m {}'.format(__spec__.name.partition('.')[0])
)
