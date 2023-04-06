import os
from test import support

print(os.environ.get("HOME"))

with support.EnvironmentVarGuard() as env:
   env.unset("HOME")
   env.set("HOME", "foo")

print(os.environ.get("HOME"))