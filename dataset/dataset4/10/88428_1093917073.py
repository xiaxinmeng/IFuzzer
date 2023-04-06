def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    tarinfo.mtime = 1
    return tarinfo

with tarfile.open(tar_reset, "w:xz") as tar_obj:
    tar_obj.add("/tmp/a", arcname="a", filter=reset)