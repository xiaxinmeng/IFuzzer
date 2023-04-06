for name, mod in sys.modules.items():
    if name != 'encodings':
        mod.__dict__["__blob__"] = Blob(name)
del name, mod, Blob