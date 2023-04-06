for buf in filedata:
    asc.resume_writing()
    asc.transport.write(buf)
    asc.pause_writing()