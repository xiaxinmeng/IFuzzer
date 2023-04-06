from PyQt5.QtCore import QObject

def run():
    obj = QObject()
    for _ in range(202):
        obj.destroyed.connect(lambda: None)

run()