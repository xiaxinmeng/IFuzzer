import sys
class MyStderr:
    def write(self, s):
        sys.stderr = None
sys.stderr = MyStderr()
1/0