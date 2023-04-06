pytb
# Ɪ know, if Ɪ press enter key while input(), the method will be completed and return a str value.
# Ɪ am trying to insert newline characters as normal characters while input() method.
# The “normal characters” means:
# 1. It can be deleted by backspace(“\x7b”) or EOF or delete key.
# 2. It can be interprered as a normal byte.
# Ɪ tried by the readline module, it did work. But it may crash, like:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# SyntaxError: multiple statements found while compiling a single statement
