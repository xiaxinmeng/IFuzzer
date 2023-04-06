import inspect

def test_func():
    ...  # This should not get printed

class Test:
    frame = inspect.currentframe()

print(inspect.getsource(Test.frame))  # Depends on findsource