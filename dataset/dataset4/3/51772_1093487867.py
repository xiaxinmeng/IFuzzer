if hasattr(socket, "SOCK_CLOEXEC") and fcntl:
    tests.append(CloexecLinuxConstantTest)