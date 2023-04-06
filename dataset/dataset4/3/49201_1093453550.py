import os
from test import support

with support.EnvironmentVarGuard() as env:
   env.unset("HOME")
   env.set("HOME", "bar")

print(os.environ.get("HOME"))