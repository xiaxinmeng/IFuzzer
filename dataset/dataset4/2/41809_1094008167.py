subprocess.Popen(["ls"], close_fds=1, preexec_fn=lambda:
os.urandom(4))