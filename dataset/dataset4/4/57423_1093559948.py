from cmd import Cmd

class FooShell(Cmd):
	def do_EOF(self, args):
		# exit on EOF
		raise SystemExit()

shell = FooShell()
shell.cmdloop()