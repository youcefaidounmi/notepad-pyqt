# src for examples : https://programtalk.com/python-more-examples/

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

# load ui
from PyQt6 import uic

# show incons
""" cmd: pyside6-rcc icons.qrc -o icons.py 
    main.py -> import icons """
import icons


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # load ui
        """ src: https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html """
        self.ui = uic.loadUi("ui/uimain.ui")

        # show ui
        self.ui.show()

        # save File
        self.ui.actionSave.triggered.connect(self.saveFile)

    # save File
    def saveFile(self):
        """ src: https://doc-snapshots.qt.io/qt6-dev/qfiledialog.html#getSaveFileName """
        try:
            fileName = QFileDialog.getSaveFileName(self, "Save file")
            """ fileName -> [path, ext] """
            if fileName[0]:
                """ w -> write"""
                file = open(fileName[0], "w")
                text = self.ui.textEdit.toPlainText()
                file.write(text)
                file.close()
            QMessageBox.about(self, "Save file", "save done. \n \f path: " +fileName[0])
        except Exception as error:
            print(error)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
