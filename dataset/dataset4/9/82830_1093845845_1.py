def askokcancel(title=None, message=None, **options):
    "Ask if operation should proceed; return true if the answer is ok"
    s = _show(title, message, QUESTION, OKCANCEL, **options)
    return s == OK