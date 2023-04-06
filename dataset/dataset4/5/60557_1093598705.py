def get_shell():
    for path in confstr("CS_PATH").split(pathsep):
        sh = sep.join((path, "sh"))
        try:
            mode = stat(sh).st_mode
        except OSError:
            pass
        else:
            if st.S_ISREG(mode):
                return sh
    raise FileNotFound("sh")