import sys
import traceback
sys.stdout = open("sob", "wb")  # WSGI sez data should be binary, so stdout should be binary???
import cgitb
sys.stdout.write(b"out")
fhb = open("fhb", "wb")
cgitb.enable()
fhb.write("abcdef")  # try writing non-binary to binary file.  Expect an error, of course.