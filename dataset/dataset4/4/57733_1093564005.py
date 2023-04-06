e = os.environ.copy()
e['PATH_TO_MY_APPS'] = "path/to/my/apps"

p = subprocess.Popen(sys.executable + " test1.py 123", env=e, shell=True, stdout=subprocess.PIPE)