with ExitStack() as stack:
 i = stack.enter_context(f())
 i = stack.enter_context(f())
 i = stack.enter_context(f())
 print(i)