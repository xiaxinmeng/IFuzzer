custom_format = argparse.CustomHelpFormat()
custom_format.indent_increment = 4
custom_format.raw_description = True
parser = argparse.ArgumentParser(formatter_class=custom_format)