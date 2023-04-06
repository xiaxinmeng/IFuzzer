
def except_global_before():
    global bar
    try:
        pass
    except Exception as bar:
        pass
