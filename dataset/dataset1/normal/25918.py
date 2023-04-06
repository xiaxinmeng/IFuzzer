source = '''

class Test(object):

    tests = []


'''

from lib2to3.refactor import RefactoringTool


def main():
    tool = RefactoringTool([])
    tool.refactor_string(source, '')
