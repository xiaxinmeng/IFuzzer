import errno
import importlib
import io
import os
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import script_helper
from test.support import socket_helper
from test.support import warnings_helper
import sched
import importlib
import test_support

@unittest.skipUnless(hasattr(os, 'fork'), 'test requires os.fork')
def test_temp_dir__forked_child():
    """Test that a forked child process does not remove the directory."""
    script_helper.assert_python_ok('-c', textwrap.dedent('\n            import os\n            from test import support\n            from test.support import os_helper\n            with os_helper.temp_cwd() as temp_path:\n                pid = os.fork()\n                if pid != 0:\n                    # parent process\n\n                    # wait for the child to terminate\n                    support.wait_process(pid, exitcode=0)\n\n                    # Make sure that temp_path is still present. When the child\n                    # process leaves the \'temp_cwd\'-context, the __exit__()-\n                    # method of the context must not remove the temporary\n                    # directory.\n                    if not os.path.isdir(temp_path):\n                        raise AssertionError("Child removed temp_path.")\n        '))

TestSupport = test_support.TestSupport()
test_temp_dir__forked_child()
