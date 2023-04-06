
try:
    compile("invalid(", "<stdin>", "single")
except Exception:
    # raise
    __import__("traceback").print_exc()
