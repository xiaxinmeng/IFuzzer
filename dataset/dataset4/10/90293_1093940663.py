import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QFrame
def update_label():
    l1.setText("Bye!")
    l1.update()
    window.repaint()
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
window.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
window.setFixedSize(800, 600)
font = QFont()
font.setPointSize(72)
l1 = QLabel(window)
l1.setText("Hello World")
l1.setFont(font)
l1.setStyleSheet("color:red")
window.show()
timer = QTimer()
timer.setInterval(1000)
timer.timeout.connect(update_label)
timer.start()
app.exec()