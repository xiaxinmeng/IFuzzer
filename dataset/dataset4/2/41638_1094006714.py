def get_current_dir_name():
    cwd = os.getcwd()
    
    try:
        pwd = os.environ["PWD"]
    except KeyError:
        return cwd