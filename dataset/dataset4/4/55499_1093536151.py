def fix_tcl_error(s):

    if '\\' in s and not ' ' in s:
        s = '{'+s+'}'

    return s