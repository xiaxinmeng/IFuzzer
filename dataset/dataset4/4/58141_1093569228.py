# This string includes all chars that may be in a file name (without a path
# separator)
FILENAME_CHARS = string.ascii_letters + string.digits + os.curdir + "._~#$:-"
# This string includes all chars that may be in an identifier
ID_CHARS = string.ascii_letters + string.digits + "_"