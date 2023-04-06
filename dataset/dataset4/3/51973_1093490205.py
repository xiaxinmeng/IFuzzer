f = os.path.join(d, "db.h")
if sys.platform == "darwin" and is_macosx_sdk_path(d):
   f = os.path.join(sysroot, d[1:], "db.h")