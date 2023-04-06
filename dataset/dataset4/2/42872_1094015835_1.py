with open(myfilename, ...) as myfile:
    while 1:
        myfile.write(...)
        myfile.flush()
        myfile.seek(0)
        do_stuff_with(myfilename)
        myfile.truncate()