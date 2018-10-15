import sys
from PyQt5.QtWidgets import * #QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import  *
from PyQt5.QtCore import QDir, Qt, QUrl, QTime
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
        exitButton.triggered.connect(self.closeInterface)

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

        # State bar
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0,0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        # Timer
        self.timer = QLabel('00:00:00')
        self.timer.setFixedWidth(60)
        self.timer.setFixedHeight(10)
        self.timer.setUpdatesEnabled(True)




        # Error Label
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)


        # Create layout to control panel
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0,0,0,0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
        controlLayout.addWidget(self.timer)

        # -------------------------------------

        # Create a widget for windows contents
        windowVideo = QWidget(self)
        videoWidget = QVideoWidget()

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChangedIcon)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.setCentralWidget(windowVideo)

        # -------------------------------------
        # Group Box Select Temps
        # -------------------------------------
        

        #-------------------------------------
        # Create layout all interface
        #-------------------------------------
        layoutInterface = QVBoxLayout()
        layoutInterface.addWidget(videoWidget)
        layoutInterface.addLayout(controlLayout)
        layoutInterface.addWidget(self.errorLabel)

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
            self.errorLabel.setText('')#If video is ok, update content in error label.
        return

    def closeInterface(self):
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

    # Position Slider
    def setPosition(self,position):
        self.mediaPlayer.setPosition(position)
        return
    def positionChanged(self,position):
        self.positionSlider.setValue(position)
        # This update time label from position in ms
        mtime = QTime(0,0,0,0)
        mtime = mtime.addMSecs(self.mediaPlayer.position())
        self.timer.setText(mtime.toString())
        return
    def durationChanged(self,duration):
        self.positionSlider.setRange(0,duration)
        return

    # Error
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error:" + self.mediaPlayer.errorString())
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Launching...")
    gui = ApplicationVideo()
    gui.initUI()
    gui.show()
    sys.exit(app.exec_())
