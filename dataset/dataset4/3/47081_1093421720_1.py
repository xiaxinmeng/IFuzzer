#comment
#-*- coding: windows-1251 -*-
from traceback import extract_stack
print("this is line", extract_stack()[-1][1])