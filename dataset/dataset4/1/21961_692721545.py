
import _ast
from test.support import run_in_subinterp
run_in_subinterp('import _ast; _ast.Constant.x=1')
print(_ast.Constant.x)
