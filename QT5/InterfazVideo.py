import sys
from PyQt5.QtWidgets import * #QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import  *
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class ApplicationVideo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Interfaz Video'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        return

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

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

        #-----------------------------------
        # Control panel
        #----------------------------------

        # Play button
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)


        # Create layout to control panel
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0,0,0,0)
        controlLayout.addWidget(self.playButton)

        # -------------------------------------

        # Create a widget for windows contents
        windowVideo = QWidget(self)
        videoWidget = QVideoWidget()

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChangedIcon)
        self.setCentralWidget(windowVideo)

        #-------------------------------------
        # Create layout all interface
        #-------------------------------------
        layoutInterface = QVBoxLayout()
        layoutInterface.addWidget(videoWidget)
        layoutInterface.addLayout(controlLayout)

        windowVideo.setLayout(layoutInterface)
        return

    def openFile(self):
        print("Choose file to open")
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose a video", QDir.homePath())
        print("Opening: %s" % fileName)
        if fileName != '':
            url = QUrl.fromLocalFile(fileName)
            self.mediaPlayer.setMedia(QMediaContent(url))
            self.playButton.setEnabled(True)

        return

    def close(self):
        print("Closing app...")
        sys.exit(0)

    def play(self):
        # Change the state of video from play to pause. To change icon, call mediaStateChanged
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            print("Pause video...")
        else:
            self.mediaPlayer.play()
            print("Play video...")
        return

    # Change icon play/pause.
    def mediaStateChangedIcon(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Launching...")
    gui = ApplicationVideo()
    gui.initUI()
    gui.show()
    sys.exit(app.exec_())
