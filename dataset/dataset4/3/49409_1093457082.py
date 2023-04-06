if not required_extension_loaded:
    extlib = os.environ.get('OPTIONAL_VAR_THAT_POINTS_TO_EXT')
    if extlib:
        master.tk.eval('global auto_path; '
                       'lappend auto_path {%s}' % extlib)
    master.tk.call('package', 'require', 'Extlibname')
    required_extension_loaded = True