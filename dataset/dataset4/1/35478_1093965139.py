class Directory (_Dialog):
    command = "tk_chooseDirectory"

def choose_directory (**options):
    return apply(Directory, (), options).show()