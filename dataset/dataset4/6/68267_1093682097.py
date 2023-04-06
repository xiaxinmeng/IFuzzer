def innertext(elt):
    return (elt.text or '') +''.join(innertext(e)+(e.tail or '') for e in elt)