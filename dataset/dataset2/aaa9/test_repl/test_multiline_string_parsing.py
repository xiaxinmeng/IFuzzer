import sys
import os
import unittest
import subprocess
from textwrap import dedent
from test.support import cpython_only, SuppressCrashReport
from test.support.script_helper import kill_python
import test_repl

@cpython_only
def test_multiline_string_parsing():
    user_input = '        x = """<?xml version="1.0" encoding="iso-8859-1"?>\n        <test>\n            <Users>\n                <fun25>\n                    <limits>\n                        <total>0KiB</total>\n                        <kbps>0</kbps>\n                        <rps>1.3</rps>\n                        <connections>0</connections>\n                    </limits>\n                    <usages>\n                        <total>16738211KiB</total>\n                        <kbps>237.15</kbps>\n                        <rps>1.3</rps>\n                        <connections>0</connections>\n                    </usages>\n                    <time_to_refresh>never</time_to_refresh>\n                    <limit_exceeded_URL>none</limit_exceeded_URL>\n                </fun25>\n            </Users>\n        </test>"""\n        '
    user_input = dedent(user_input)
    p = test_repl.spawn_repl()
    p.stdin.write(user_input)
    output = kill_python(p)
    TestInteractiveInterpreter.assertEqual(p.returncode, 0)

TestInteractiveInterpreter = test_repl.TestInteractiveInterpreter()
test_multiline_string_parsing()
