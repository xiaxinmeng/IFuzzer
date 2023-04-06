
import sys
import io

def import_ok(name):
    try:
        __import__(name)
    except ImportError:
        return False
    else:
        return True

stdout = sys.stdout
stderr = sys.stderr

for name in sys.module_names:
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    ok = import_ok(name)
    sys.stdout = stdout
    sys.stderr = stderr
    print(f"{name}: {ok}")
