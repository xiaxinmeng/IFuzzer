for ob in builtins.__dict__.values():
    if (str(ob).startswith('<class') and
        ob.__init__.__text_signature__ is None):
        print(ob)
# prints nothing.