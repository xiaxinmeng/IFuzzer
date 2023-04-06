f = open('broken.py','w')
f.write("1 = a  #<-- obvious syntax err\n")
f.close()
import py_compile
py_compile.compile('broken.py')