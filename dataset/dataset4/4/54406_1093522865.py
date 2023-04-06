def escapeargs(*args):
   return ' '.join(pipes.quote(arg) for arg in args)