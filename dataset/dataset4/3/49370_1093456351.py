def _load_tile(master):
    if _REQUIRE_TILE:
        import os
        tilelib = os.environ.get('TILE_LIBRARY')
        if tilelib:
            # append custom tile path to the the list of directories that
            # Tcl uses when attempting to resolve packages with the package
            # command
            master.tk.eval(
                    'global auto_path; '
                    'lappend auto_path {%s}' % tilelib)

        master.tk.eval('package require tile') # TclError may be raised here
        master._tile_loaded = True