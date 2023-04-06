
def except_global_after():
    try:
        pass
    except Exception as bar:
        pass
    global bar
