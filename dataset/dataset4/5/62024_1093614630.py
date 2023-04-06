import pty
for i in range(N):
    try: pty.spawn(["/non-existent"])
    except: pass