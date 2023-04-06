if "PYTHONEXECUTABLE" in os.environ:
    executable = os.environ["PYTHONEXECUTABLE"]
else:
    executable = sys.executable