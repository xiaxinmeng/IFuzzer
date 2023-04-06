import tempfile

hello = bytes('Hello World!', encoding='utf-8')
tf = tempfile.TemporaryFile()
stf = tempfile.SpooledTemporaryFile()

tf.write(hello)
stf.write(hello)