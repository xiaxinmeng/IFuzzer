code = "42 if True else 43\n" * 200000
compile(code, "foobar", "exec")