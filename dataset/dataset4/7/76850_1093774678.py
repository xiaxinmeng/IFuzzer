
import cgitb
import sys

try:
    f = open('non_exitant_file_path.foo')
except Exception as e:
    cgitb.text(sys.exc_info())
