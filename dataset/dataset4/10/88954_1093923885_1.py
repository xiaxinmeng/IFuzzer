def use_func1(f: Callable[Concatenate[int, P], None]) -> None:
  ...

def use_func2(f: Callable[Concatenate[int, ...], None]) -> None:
  ...