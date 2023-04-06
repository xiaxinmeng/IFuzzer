if p2cread != -1 and p2cwrite != -1 and p2cread != devnull_fd:
    os.close(p2cread)