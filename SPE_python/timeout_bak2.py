import multiprocessing.pool
import functools
  


def set_timeout(max_timeout,callback):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            try: 
                pool = multiprocessing.pool.ThreadPool(processes=1)
                async_result = pool.apply_async(item, args, kwargs)
                # raises a TimeoutError if execution exceeds max_timeout
                return async_result.get(max_timeout)
            except:
                callback()
        return func_wrapper
    return timeout_decorator

def after_timeout():
  print("time out..........")