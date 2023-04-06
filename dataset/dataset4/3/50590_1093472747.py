import os

def show_cwd_list():
    alpha = os.listdir(os.getcwd())
    for dirnm in alpha[:]:
        if os.path.isdir(os.getcwd() + os.sep + dirnm):
            print("d ", dirnm)
        elif os.path.ismount(os.getcwd() + os.sep + dirnm):
            print("m ", dirnm)
        elif os.path.isfile(os.getcwd() + os.sep + dirnm):
            print("f ", dirnm)
        elif os.path.islink(os.getcwd() + os.sep + dirnm):
            print("l ", dirnm)
        elif os.path.isabs(os.getcwd() + os.sep + dirnm):
            print("a ", dirnm)
    return alpha

get_dirs()