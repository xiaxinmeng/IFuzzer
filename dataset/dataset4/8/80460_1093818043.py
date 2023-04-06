p = os.popen('sleep 1234')
os.wait3(os.WNOHANG)
os.wait3(os.WNOHANG)
os.wait3(os.WNOHANG)