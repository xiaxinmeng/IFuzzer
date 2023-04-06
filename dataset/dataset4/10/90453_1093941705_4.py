from test.support import run_in_subinterp
run_in_subinterp("""
import sys
sys.path.append(".")
import native_ext
native_ext.run_simple()
""")