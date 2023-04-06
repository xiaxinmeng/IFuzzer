MAXLINESIZE = 76 # Excluding the CRLF
MAXBINSIZE = (MAXLINESIZE//4)*3  # 57
...
while True:
    s = input.read(MAXBINSIZE)
    if not s:
        break
    line = binascii.b2a_base64(s)
    output.write(line)