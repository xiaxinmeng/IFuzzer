import io
rawio = io.BytesIO(b"abc")
bufio = io.BufferedReader(rawio)
while True:
    bufio.__init__(rawio)