def _format_locals(filename, lineno, name, locals):
    return {k: repr(v) for k,v in locals.items() if not k.endsswith("_sensitive")}