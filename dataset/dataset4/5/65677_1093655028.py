from unittest import mock

def foo(a, b):
    pass

parent = mock.Mock()
a = mock.create_autospec(foo)
parent.child = a # 'a' is FunctionType and has a.mock attribute set (create_autospec -> _set_signature -> _setup_func)

parent.child_func = foo # 'foo' is FunctionType with no mock attribute set that could cause AttributeError

parent.child(1, 2) # Recorded
parent.child_func(2, 3) # Not recorded since it's actual call to child_func and has no parent set due to AttributeError
print(parent.method_calls) # [call.child(1, 2)]