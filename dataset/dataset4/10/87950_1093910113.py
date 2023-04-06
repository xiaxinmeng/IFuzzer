class SubprocTest(object):
	def run(self):
		print("run")
		proc_args = ["cmd.exe"]
		self._process = subprocess.Popen(proc_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	def __del__(self):
		print("__del__")
		if self._process is not None:
			self.terminate()
	
	def terminate(self):
		print("terminate")
		self._process.communicate(input=b"exit\n", timeout=1)
		print("kill")
		self._process.kill()
		self._process = None

if __name__ == "__main__":
	s = SubprocTest()
	s.run()
	del s
	print("s done")
	
	t = SubprocTest()
	t.run()
	print("t done")