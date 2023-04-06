from unittest import TestSuite, TestLoader, TextTestRunner
from sys import exit

def loadTests(loader):
    """Generator listing all test cases"""
    ...

def main():
    loader = TestLoader()

    suite = TestSuite()
    for test in loadTests(loader.loadTestsFromTestCase):
        suite.addTests(test)

    runner = TextTestRunner(descriptions=2, verbosity=2)
    result = runner.run(suite)
    if result.failures or result.errors:
        exit(1)