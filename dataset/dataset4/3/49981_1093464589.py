if self.plat_name == 'win32':
    sfix = ''
else:
    sfix = self.plat_name[3:] # strip 'win' - leaves eg '-amd64'
filename = os.path.join(directory, "wininst-%.1f%s.exe" % (bv, sfix))
return open(filename, "rb").read()