class ViewChanger(Tkinter.StringVar) :

    def __init__(self, views) :
        self.views = views
        Tkinter.StringVar.__init__(self)

    def set(self, newview) :
        self.views.activate(newview)
        Tkinter.StringVar.set(newview)