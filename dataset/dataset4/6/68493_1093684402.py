if sys.version_info.major == 3 and sys.version_info.minor == 4:
  stacklevel = 8
elif  sys.version_info.major == 3 and sys.version_info.minor == 4:
  stacklevel = 10
else:
  stacklevel = 2 # I bet they fixed it in 3.6!