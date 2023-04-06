with socket.socket(socket.AF_INET, socket.SOCK_STREAM|socket.SOCK_CLOEXEC) as s:
    print(bool(fcntl.fcntl(s, fcntl.F_GETFD) & fcntl.FD_CLOEXEC))