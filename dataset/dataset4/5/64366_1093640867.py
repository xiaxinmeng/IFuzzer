for seq, id in self.handlerids:
    try:
        self.widget.unbind(self.widgetinst, seq, id)
    except _tkinter.TclError:
        break