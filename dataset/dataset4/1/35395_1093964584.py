import sys, os

if not os.environ.has_key('TCL_LIBRARY'):
    tcl_library = os.path.join(sys.prefix, "tcl", "tclX.Y")
    os.environ['TCL_LIBRARY'] = tcl_library