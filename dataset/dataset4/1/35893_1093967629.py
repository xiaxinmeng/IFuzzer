code = "def foo():\n  pass"
open("bug.py", "w").write(code)
import bug # works
compile(code, "<string>", "exec") # doesn't work