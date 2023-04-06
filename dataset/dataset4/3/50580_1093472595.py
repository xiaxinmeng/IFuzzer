scripts = ['Unknown']
def findscript(script):
  try:
    return scripts.index(script)
  except ValueError:
    scripts.append(script)
    return len(scripts)-1