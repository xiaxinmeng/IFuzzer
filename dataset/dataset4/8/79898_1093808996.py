code = "from enum import Enum; Enum('Animal', 'ANT BEE CAT DOG')"
code = compile(code, "<string>", "exec")
global_ns = {}
local_ls = {}
exec(code, global_ns, local_ls)