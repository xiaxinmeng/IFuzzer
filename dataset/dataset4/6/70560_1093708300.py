sp = subprocess.Popen('cat --not-an-option', shell=True, stdin=subprocess.PIPE)
time.sleep(.2)
sp.communicate(b'hi\n')