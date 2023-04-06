with tempfile.TemporaryFile(dir="/vagrant") as tf:
    tf.write("testing testing testing\n".encode('utf-8'))