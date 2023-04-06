from dis import dis
def dis_str(source):
  modes = ('eval', 'single', 'exec')
  for mode in modes:
    try:
      c = compile(source, '', mode)
      break
    except SyntaxError:
      if mode is modes[-1]:
        raise
  return dis(c)