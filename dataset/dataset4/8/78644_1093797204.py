import traceback
import sys

se = SyntaxError("wrong!")
se.filename = "myfile.py"
print("========== lineno is None ==========")
print('traceback.print_exception:')
traceback.print_exception(type(se), se, None)
print('---------------------')
print('sys.excepthook:')
sys.excepthook(type(se), se, None)
print('---------------------')

se.lineno = 55

print("========== lineno is 55 ==========")
print('traceback.print_exception:')
traceback.print_exception(type(se), se, None)
print('---------------------')
print('sys.excepthook:')
sys.excepthook(type(se), se, None)
print('---------------------')