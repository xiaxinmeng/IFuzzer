_inidle = type(sys.stdin) == types.InstanceType and \
	  sys.stdin.__class__.__name__ == 'PyShell'