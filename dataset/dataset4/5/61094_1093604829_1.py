def delete_recursive(parent):
    for child in parent.childNodes:
        if child.hasChildNodes():
            delete_recursive(child)
        else:
            parent.removeChild(child)

delete_recursive(dom)