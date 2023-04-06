def foo() -> int:
    with raises_on_exit() as mgr:
        return 'a'
        pass