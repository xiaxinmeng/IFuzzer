import tarfile
import os

for f in ["foo.txt", "foo.tar"]:
    try:
        os.unlink(f)
    except OSError:
        pass

with open("foo.txt", "w") as f:
    f.write("foo.txt")
    with tarfile.open("foo.tar", "w:gz") as tarfile_obj:
        tarfile_obj.add(f.name)

with tarfile.open("foo.tar", "r:gz") as f:
    member = f.extractfile("foo.txt")
    print(f"Has attr : {hasattr(member, 'fileno')}")
    print(member.fileno())