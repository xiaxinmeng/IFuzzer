CODE = """
import runpy
import sys
import traceback
sys.argv = ["pip", "list"]
try:
    runpy.run_module("pip", run_name="__main__", alter_sys=True)
except SystemExit:
    pass
except Exception as exc:
    traceback.print_exc()
    print("BUG", exc)
    raise
"""