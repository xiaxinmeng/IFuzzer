class CLI(cmd.Cmd):
   def register_subcommand(self, cmd, cli_class):
       def call_cli(self):
           cli = cli_class()
           cli.cmdloop()
       setattr(self, 'do_%s' % (cmd, ), call_cli)