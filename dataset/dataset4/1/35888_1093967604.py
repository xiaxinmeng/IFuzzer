from Tkinter import *

root = Tk()

log = open("log.txt","w")

## Force crash by generating too many PhotoImage objects
images = []
for i in xrange(0,10000):
    if i>9900:
        log.write( str(i)+"\n" )
        log.flush()
    image = PhotoImage()
    image.put("blue")
    images.append( image )