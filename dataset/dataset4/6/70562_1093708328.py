def james_map(exe, fn, *args):
  return iter( sorted( list( exe.map( fn, *args ) ) ) )