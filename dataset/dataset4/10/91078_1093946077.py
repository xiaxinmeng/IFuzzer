import io
import tarfile

# Create a tarball with no member:
fd = io.BytesIO()
with tarfile.open(fileobj=fd, mode="w") as tf:
    pass

# read in stream mode:
fd.seek(0)
with tarfile.open(fileobj=fd, mode="r|") as tf:
    print(tf.next())   # tarfile.StreamError: seeking backwards is not allowed

# read in normal mode:
fd.seek(0)
with tarfile.open(fileobj=fd, mode="r") as tf:
    print(tf.next())  # ValueError: negative seek value -1