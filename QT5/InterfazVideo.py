import sys
from PyQt5.QtWidgets import * #QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        return

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        videoWidget = QVideoWidget()

        # Create Open Action
        openButton = QAction('&Open',self)
        openButton.setShortcut('Cmd+o')
        openButton.setStatusTip('Open movie')
        openButton.triggered.connect(self.openFile)

        # Create Exit Action Button
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Cmd+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        # Create Menu Bar
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)  # It's necessary if you are working in OS. Unless, MenuBar doesn't appear.
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(openButton)
        fileMenu.addAction(exitButton)

        # Create a widget for windows contents
        windowVideo = QWidget(self)
        self.setCentralWidget(windowVideo)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)

        windowVideo.setLayout(layout)

        return

    def openFile(self):
        print("Choose file to open")
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose a video", QDir.homePath())
        print("Opening: %s" % fileName)
        return


    def close(self):
        print("Closing app...")
        sys.exit(0)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Launching...")
    gui = App()
    gui.initUI()
    gui.show()
    sys.exit(app.exec_())
