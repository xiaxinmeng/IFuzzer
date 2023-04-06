from functools import wraps

def log_info(func: Callable[P, R]) -> Callable[P, R]:
  @wraps
  def _log_func(*args: P.args, **kwargs: P.kwargs) -> R:
    print("stuff")
    return func(*args, **kwargs)

  return _log_func

@log_info
def foo(x: int) -> str:
  ...