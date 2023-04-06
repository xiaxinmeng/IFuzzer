if os.path.normcase(os.getcwd()) == os.path.normcase(sys.prefix):
    os.chdir(get_default_location(sys.platform))