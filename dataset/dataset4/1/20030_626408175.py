
for suffix in "", "\n", "\n\n":
    try:
        compile("raise=1" + suffix, "", "exec")
    except SyntaxError as err:
        print(repr(err))
