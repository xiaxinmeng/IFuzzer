# first line
import inspect
frame = inspect.currentframe()
print(frame.f_code.co_firstlineno)
print(inspect.findsource(frame.f_code))