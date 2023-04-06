import os, tempfile
with tempfile.TemporaryDirectory() as d:
	os.symlink("/proc", d + "/test")