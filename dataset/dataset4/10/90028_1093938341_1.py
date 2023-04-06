readline.clear_history()
readline.read_history_file("history.txt")

class MyShell(cmd.Cmd):
    def __init__(self):
        super().__init__()

shell = MyShell()
shell.cmdloop()