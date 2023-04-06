time.sleep(1)
subprocess.call([sys.executable, '-c', ''], stdin=r)

os.close(w)
p1.wait()