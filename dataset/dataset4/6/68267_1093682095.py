def innertext(elt):
    return (elt.text or '') +''.join(innertext(e)+e.tail for e in elt)