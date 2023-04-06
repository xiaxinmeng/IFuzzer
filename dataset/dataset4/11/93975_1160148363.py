def foo() -> int:
    with open('/dev/null') as devnull:
        return len("a")