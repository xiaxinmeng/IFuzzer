import sys
import inspect

sys.setrecursionlimit(50)


def except_works() -> None:
    raise Exception


try:
    except_works()
except Exception as e:
    print("Exception was:", e)


def funcy(depth: int) -> None:
    print(f"Stack depth is:{len(inspect.stack())}")
    if depth == 0:
        return
    funcy(depth - 1)


try:
    funcy(60)
except Exception as e:
    print("Exception was:", e)

print("This executes without the debugger navigating to it.")