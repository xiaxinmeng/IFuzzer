editor = self.parentGui.flist.open(file)
editor.set_close_hook(lambda self=self:
self.parentGui.close_idle(self))
self.editor = editor