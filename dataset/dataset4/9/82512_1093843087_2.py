def func():
    print(var)

my_globals = {'func':func,'var':14}
exec("def func():\n    print(var)\nprint(var);func()",my_globals,my_globals)