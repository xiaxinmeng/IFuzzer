fd = os.open("document.txt", os.O_WRONLY | os.O_CREAT, 0o777)
fp = open(fd, "wb")
with fp:
   ...