import inspect

def hello():
    print("Hello World")

print(inspect.getsource(hello))

class Hello:
    def __init__(self):
        print("Hello World")

print(inspect.getsource(Hello))