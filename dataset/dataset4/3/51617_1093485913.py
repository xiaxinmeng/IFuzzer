def _core(func, my_args):
    A = Thread(target = func, args = my_args); A.start(); A.join()
_core(ask_user, (question, default_answer))