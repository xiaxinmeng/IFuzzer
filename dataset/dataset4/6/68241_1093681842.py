# process files and store errors in a list
sys.exit(len(errors))  # bad - success for multiples of 256 errors
sys.exit(sys.EXIT_SUCCESS if not errors else sys.EXIT_FAILURE)  # good