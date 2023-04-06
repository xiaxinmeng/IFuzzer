def open(self, url, new=1):
 # XXX currently I know no way to prevent KFM from opening a new win.
 #self.open_new(url)
 os.system("dcop konqueror KonquerorIface getWindows >/dev/null")
 cmd="dcop konqueror konqueror-mainwindow#1 openURL %s >/dev/null" % url
 os.system(cmd)