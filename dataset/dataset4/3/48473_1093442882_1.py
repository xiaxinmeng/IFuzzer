import sys
import inspect

sys.path.append('aaa.zip')
import aa

inspect.getsource(aa.x)
inspect.getsource(aa.y)