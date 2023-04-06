tgtdir = os.path.dirname(tgt)
if not os.path.exists(tgtdir):
    os.makedirs(tgtdir)
with open(tgt, 'wb') as fp:
    fp.write(zf.read(path))