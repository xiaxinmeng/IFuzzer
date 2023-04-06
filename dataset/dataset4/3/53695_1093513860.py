import readline
readline.clear_history()
readline.add_history("first line")
readline.add_history("second line")
while True:
    readline.replace_history_item(0, "replaced item")