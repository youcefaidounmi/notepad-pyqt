import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
# load ui
from PySide6.QtCore import QFile, QIODevice
from PyQt6 import uic
# show incons => cmd: pyside6-rcc icons.qrc -o icons.py
import icons
import os
import stat

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # connect to ui => src: https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
        self.ui = uic.loadUi("ui/uimain.ui")

        # show ui =======================
        self.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
