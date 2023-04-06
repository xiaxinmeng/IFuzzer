def doXY ():
  # ...
  try:
    page = urlopen( someRequest )
  except urllib.error.URLError as e:
    raise MyError( 'while doing XY', e )
  # ...