
import sys
import subprocess    
import ast

_PYTHON_INFO_SCRIPT = """import platform, sys, os, sysconfig
_executable = os.path.normcase(os.path.abspath(getattr(sys, "_base_executable", sys.executable)))
_platform = sys.platform
if _platform == "linux2":
    _platform = "linux"
print({
    "_platform": _platform,
    "_os_name": os.name,
    "_executable": (_executable, ),
    "_exec_dir": os.path.normcase(os.path.abspath(os.path.dirname(_executable))),
    "_name": platform.python_implementation(),
    "_type": platform.python_implementation().lower(),
    "_version": tuple(sys.version_info),
    "_is_pypy": "__pypy__" in sys.builtin_module_names,
    "_is_64bit": (getattr(sys, "maxsize", None) or getattr(sys, "maxint")) > 2 ** 32,
    "_versioned_dir_name": "%s-%s" % (platform.python_implementation().lower(), ".".join(str(f) for f in sys.version_info)),
    "_environ": dict(os.environ),
    "_darwin_python_framework": sysconfig.get_config_var("PYTHONFRAMEWORK")
})
"""

result = subprocess.check_output([sys.executable, "-c", _PYTHON_INFO_SCRIPT], universal_newlines=True)
python_info = ast.literal_eval(result)
print(python_info)

