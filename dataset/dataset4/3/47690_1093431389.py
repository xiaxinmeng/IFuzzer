import sys
import os
import subprocess

command = ('''%s -c "import os; print os.environ['YAHOO']"''' %
           sys.executable)

env = {"YAHOO": "ABCDE", "SystemRoot": os.environ["SystemRoot"]}
subprocess.Popen(command, env=env).wait()