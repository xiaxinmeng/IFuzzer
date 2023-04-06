src = pathlib.Path('dir1/file')
dst = pathlib.Path('dir2/file')
os.symlink(src, dst) # or dst.symlink_to(src)