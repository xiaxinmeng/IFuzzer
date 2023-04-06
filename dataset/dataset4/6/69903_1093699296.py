import tempfile

with tempfile.TemporaryFile(dir="/tmp") as tf:
    tf.write("testing testing testing\n".encode('utf-8'))
print("Temp file: worked")