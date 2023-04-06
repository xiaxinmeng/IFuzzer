closed_fd = os.open("/dev/null", os.O_RDONLY);
os.close(closed_fd)