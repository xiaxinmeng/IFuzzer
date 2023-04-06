def unbind(widget, seq, funcid):
    bindings = {x.split()[1][3:]: x for x in widget.bind(seq).splitlines() if x.strip()}
    try:
        del bindings[funcid]
    except KeyError:
        raise tk.TclError('Binding "%s" not defined.' % funcid)
    widget.bind(seq, '\n'.join(list(bindings.values())))