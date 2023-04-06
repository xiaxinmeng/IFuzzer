os.write(our_pipe.input, b"data")
os.read(our_pipe.output, 1024)