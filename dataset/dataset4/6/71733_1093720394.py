def tk_update():
    root.update()
    loop.call_soon(tk_update)  # or loop.call_later(delay, tk_update)