while 1:
    with open(myfilename, ...) as myfile:
        myfile.write(...)
    do_stuff_with(myfilename)
    os.remove(myfilename)