z = ZipFile('D:\\1', 'r')
zlist = z.infolist()
for zi in zlist:
    zf = z.open(zi)
    zf.close()

z.close()
os.remove(attach)