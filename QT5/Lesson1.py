import sys

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QMainWindow)
from PyQt5.QtCore import pyqtSlot # Para usar los botones
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage('Message in statusbar.') # Mensaje en la parte inferior de la ventana.
        # Add a button
        button = QPushButton('PyQt5 button',self)
        button.setToolTip('This is an example button')
        button.resize(100,20)
        button.move(100,70) # Move button to coordenates 100x y 70y

        # Clicked button
        button.clicked.connect(self.on_click)
        self.show()

    # Add event to click button
    # @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


class Dialog (QDialog):
    def slot_method(self):
        print('slot method called')

    def __init__(self):
        super(Dialog, self).__init__()

        button = QPushButton("Click")
        button.clicked.connect(self.slot_method)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example -pythonspot.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = App()
    #sys.exit(app.exec_())
    dialog = Dialog()
    sys.exit(dialog.exec_())