s = db.elset(sys.argv[1])
for t in sys.argv[2:]:
	s &= db.elset(t)