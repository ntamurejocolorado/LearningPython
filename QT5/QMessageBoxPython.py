print("Show message box in qt")

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Aplication(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messageBox'
        self.left = 20
        self.top = 20
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Eso no hace falta un lienzo, se pinta solo en una ventana al darle al yes or no
        # en este caso se cerrará y mostrará el lienzo en blanco creado arriba con self
        # que se muestra con self.show(). Si lo comentamos como el qmessage no lo necesita
        # al cerrar el qmessage no aparecerá nada.
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?",
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)

        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print("Yes clicked")
        if buttonReply == QMessageBox.No:
            print("No clicked")
        if buttonReply == QMessageBox.Cancel:
            print("Cancel clicked")

        # self.show() # Este show muestra el lienzo en blanco sobre el que pintamos.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Aplication()
    sys.exit(app.exec_())
