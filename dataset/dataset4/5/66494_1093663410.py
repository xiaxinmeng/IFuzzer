def _show_warning(message, category, filename, lineno, file=None, line=None):
    """Hook to write a warning to a file; replace if you like."""
    if file is None:
        file = sys.stderr
    try:
        file.write(formatwarning(message, category, filename, lineno, line))
    except IOError:
        pass # the file (probably stderr) is invalid - this warning gets lost.