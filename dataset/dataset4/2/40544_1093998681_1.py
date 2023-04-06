klass = eval(klass, dict(vars(logging).items() +
vars(logging.handlers).items()))
...
args = eval(args, dict(vars(logging).items() +
vars(logging.handlers).items()))