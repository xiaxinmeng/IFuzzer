def say_hello(key, count):
   ...
readline.add_defunc("say_hello", say_hello)
readline.parse_and_bind('"?" : say_hello')