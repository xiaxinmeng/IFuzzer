# give rudimentary help if nothing but prog name is entered
import os
# get program name as it is called
pnam = os.path.basename(sys.argv[0])
Use = "Usage: {0} [options]".format(pnam)
if len(sys.argv) == 1:
    print(Use)
    print("Use option '-h' for help.")
    sys.exit()