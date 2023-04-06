with open(testPath, "r+") as tFile:
    ## First we read the file 
    data = tFile.read()

    ## Now we write some data 
    tFile.write('Some Data')

    ## Now we read the file again
    tFile.read()