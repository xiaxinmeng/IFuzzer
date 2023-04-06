from unittest import mock

target = dict(a=1)

@mock.patch.dict(target, dict(b=2))
def test_with_decorator():
    print(f"target inside decorator : {target}")

def test_with_context_manager():
    with mock.patch.dict(target, dict(b=2)):
        print(f"target inside context : {target}")

target = dict(a=2)
test_with_decorator()
test_with_context_manager()