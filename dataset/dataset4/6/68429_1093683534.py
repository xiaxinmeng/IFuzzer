def browser():
    app = Gio.app_info_get_default_for_type('x-scheme-handler/https', True)
    bpath = app.get_filename()

    for candidate in webbrowser._tryorder:
        if candidate in bpath:
            return webbrowser.get(using=candidate)

    return webbrowser.get()