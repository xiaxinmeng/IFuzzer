password = None
username = 'username@domain.com'
flags = 0

val = ctypes.windll.mpr.WNetAddConnection2W(
  ctypes.byref(resource),
  password,
  username,
  flags)