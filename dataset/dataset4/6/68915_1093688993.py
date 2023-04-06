def describe (indicator):
    if readline.reading_line ():
        print ()
        print (indicator.description)
        readline.forced_update_display ()
    else:
        print (indicator.description)