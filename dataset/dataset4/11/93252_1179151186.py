from PyQt5.QtCore import QObject
import traceback

def fun():
    traceback.print_stack()
    print("========")

def run():
    obj = QObject()
    for _ in range(169):
        obj.destroyed.connect(fun)

run()