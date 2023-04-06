def func():
    print(var)

my_globals = {'func':func,'var':14}
exec("print(var);func()",my_globals,my_globals)