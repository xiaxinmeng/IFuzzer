def tk_update():
    root.update()
    loop.call_soon(tk_update)