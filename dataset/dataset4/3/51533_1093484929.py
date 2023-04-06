class MyArgumentParser(argparse.ArgumentParser):
    def format_help(self):
        help = super(MyArgumentParser, self).format_help()
        return headline + '\n' + help