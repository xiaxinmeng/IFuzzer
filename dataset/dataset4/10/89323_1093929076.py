for val in values:
    menu.add_radiobutton(label=val,
        variable=self._variable)
    if self._callback:
        menu.entryconfigure('last', command=lambda val=val: self._callback(val))