sys.stdout = os.fdopen(1, "w")  # replace with someting that can be flushed,
sys.stderr = os.fdopen(2, "w")  # using the original fd's even allows printing