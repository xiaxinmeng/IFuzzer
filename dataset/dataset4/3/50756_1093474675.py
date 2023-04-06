from dis import dis
def dis_str(source):
  try:
    c = compile(source, '', 'eval')
  except SyntaxError:
    c = compile(source, '', 'exec')
  return dis(c)