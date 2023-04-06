def ret():
  output = subprocess.check_output(['hg', 'id', '-nib'])
  print( output )
  print( output )
  print( output.strip() )
  print( output.strip().split() )

ret()