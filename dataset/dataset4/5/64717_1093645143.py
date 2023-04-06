class Mixin(QObject):
    # this overwrites QObject.timerEvent
    def timerEvent(self, e):
        print('mixed in')
        super().timerEvent(e)

class B(Mixin, QTimer):
    pass

class C(QTimer, Mixin):
    pass

event = QTimerEvent(0)

b = B()
try:
    b.timerEvent(event)
except Exception as e:
    print(e)
print('---------')
c = C()
c.timerEvent(event)