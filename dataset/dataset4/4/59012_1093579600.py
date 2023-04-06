import warnings
def filemode(mode):
    "Deprecated in this location; use stat.filemode."
    warnings.warn("The undocumented tarfile.filemode function\n"
                  "has been moved to stat and documented there.",
                   DeprecationWarning, 2)
    return stat.filemode(mode)