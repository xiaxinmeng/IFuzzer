def hook(*args):
    print(args)

sys.addaudithook(hook)

import os
os.system('echo main interpreter')

sub = _xxsubinterpreters.create()
_xxsubinterpreters.run_string(sub, "import os; os.system('echo you got pwned')", None)