if os.environ.has_key("USER_KNOWS_BETTER"): obey_user(fn)
else: desktop.open(fn)