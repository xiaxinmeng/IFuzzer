import subprocess, os, sys
os.putenv("victor=", "secret")
code = """import os; print(f"victor: {os.getenv('victor')!r}"); print(f"victor=: {os.getenv('victor=')!r}")"""
subprocess.run([sys.executable, "-c", code])