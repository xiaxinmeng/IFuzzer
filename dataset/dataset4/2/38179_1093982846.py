if sys.platform.find('win') != -1 and sys.executable.find('pythonw') != -1:

    blackhole = file(os.devnull, 'w')

    sys.stdout = sys.stderr = blackhole