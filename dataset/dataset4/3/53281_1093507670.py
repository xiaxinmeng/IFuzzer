def win_ismount(path):
  import win32file
  volume_path = win32file.GetVolumePathName(path)
  return volume_path == path # May have to ignore a trailing backslash