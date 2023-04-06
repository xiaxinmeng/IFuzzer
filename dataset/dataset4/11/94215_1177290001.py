def func():
    def inner(v): pass
    print(f"watch ((PyObject*){id(inner)})->ob_refcnt")
    inner(
        42
    )

print("s n n n j 4 exit")
import pdb; pdb.set_trace()
func()

# tc.py
# build Python with --with-pydebug
# $ gdb ./python --ex "run tc.py"
# in pdb run: "s" "n" "n" "n" "CTRL+Z"
# in gdb run the "watch" command and continue ("c" "c")
# in pdb eventually run "n j 4" "exit"