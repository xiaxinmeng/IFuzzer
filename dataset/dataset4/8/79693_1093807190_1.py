def test_with_context_manager():
    with mock.patch.dict('__main__.target', dict(b=2)):
        print(f"target inside context : {target}")

target = dict(a=2)
test_with_decorator()
test_with_context_manager()