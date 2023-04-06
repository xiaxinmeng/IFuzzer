pid = os.spawnv(os.P_NOWAIT, 'C:/WINDOWS/notepad.exe', ['notepad.exe'])
# (full path needed if not in /windows) to
pid = subprocess.Popen(['C:/WINDOWS/notepad.exe']).pid