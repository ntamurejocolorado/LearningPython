print("Start Proyect Qt and OpenCV")

import sys
import os.path
import cv2
from PyQt5.QtWidgets import * # QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QImage

from PyQt5.QtCore import * #Qt, pyqtSlot

#import numpy as np



class AplicationWebCam(QWidget):

    photo = None
    namePhoto = None
    imageInMemory = None

    def __init__(self):
        super().__init__()
        self.title = 'Application Web Cam'
        self.left = 20
        self.top = 20
        self.width = 620
        self.height = 520

        self.initInterface()

    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createPrincipalLayout()
        self.loadImage()

        self.show() # Este show muestra el lienzo en blanco sobre el que pintamos

    def createPrincipalLayout(self):
        # Layout Principal de la app contiene:
        # - Boton open image.
        # - Label Principal para la imagen.
        # - Layout Vertical para los botones de procesado de la imagen

        layoutHorizontalPrincipal = QHBoxLayout(self)

        layoutHorizontalPrincipal.addLayout(self.createLabelButtonOpenVerticalLayout())
        layoutHorizontalPrincipal.addLayout(self.createButtonsVerticalLayout())

        self.setLayout(layoutHorizontalPrincipal)

    def createLabelButtonOpenVerticalLayout(self):
        # Layout button open and label image
        layoutVertical = QVBoxLayout()

        # Button Image
        buttonOpen = QPushButton("Open Image", self)
        buttonOpen.setMaximumWidth(130)
        buttonOpen.clicked.connect(self.slot_openImage)

        # Label to show web cam
        self.labelImage = QLabel("Image...", self)
        self.labelImage.setMaximumWidth(500)
        self.labelImage.setMaximumHeight(500)
        self.labelImage.setStyleSheet('background-color: black')

        # Add layout to principal horizontal layout
        layoutVertical.addWidget(buttonOpen)
        layoutVertical.addWidget(self.labelImage)

        return layoutVertical

    def createButtonsVerticalLayout(self):
        # Aqui se muestran los 3 botones para procesar el color de la imagen
        verticalLayoutButton = QVBoxLayout()

        # Button Gray
        buttonGray = QPushButton("Gray",self)
        buttonGray.setMaximumWidth(100)
        buttonGray.clicked.connect(self.slot_grayImage)

        # Button Canny
        buttonCanny = QPushButton("Canny",self)
        buttonCanny.setMaximumWidth(100)

        # Button Red
        buttonRed = QPushButton("Red",self)
        buttonRed.setMaximumWidth(100)

        #Button Save
        buttonSave = QPushButton("Save",self)
        buttonSave.setMaximumWidth(100)
        buttonSave.clicked.connect(self.slot_saveImage)


        verticalLayoutButton.addWidget(buttonGray)
        verticalLayoutButton.addWidget(buttonCanny)
        verticalLayoutButton.addWidget(buttonRed)
        verticalLayoutButton.addWidget(buttonSave)


        return verticalLayoutButton

    def loadImage(self):
        path = "/Users/ntamurejo/Proyectos/LearningPython/LearningPython/QtOpenCV/colorBalls.png"

        if os.path.isfile(path):
            print("Existe")
            print(path)
            self.photo = QPixmap(path)
            self.labelImage.setPixmap(self.photo)

            self.imageInMemory = cv2.imread(path, 1)  # 0 grayscale, 1 in color
        else:
            print("No existe")

    def slot_grayImage(self):
        print("Gray image")
        grayImage = cv2.cvtColor(self.imageInMemory, cv2.COLOR_BGR2GRAY)
        qImageGrayImage = QImage(grayImage.data, grayImage.shape[1], grayImage.shape[0],grayImage.strides[0], QImage.Format_Indexed8)
        pixmapImageCV = QPixmap.fromImage(qImageGrayImage)
        self.labelImage.clear()
        self.labelImage.setPixmap(pixmapImageCV)

    def slot_redImage(self):
        print("RGB image")
        rgbImage = cv2.cvtColor(self.imageInMemory, cv2.COLOR_BGR2GRAY)

        # Convert cvMat to QImage
        qRGBImage = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],rgbImage.strides[0],QImage.Format_Indexed8)

        # Convert QImage to Pixmap
        pixmapRGBImage = QPixmap.fromImage(qRGBImage)
        self.labelImage.clear()
        self.labelImage.setPixmap(pixmapRGBImage)


    def slot_saveImage(self):
        self.imageInMemory = cv2.imread(self.namePhoto, 1)  # 0 grayscale, 1 in color
        cv2.imwrite("colorBalls.png", self.imageInMemory)  # This will save the image in PNG format in the working directory

    def slot_openImage(self):
        print("Choose image .png")
        fileName = QFileDialog.getOpenFileName(self, "Open file", "","All Files (*.JPG *.png *.gif)")
        self.labelImage.clear()

        # Read fileName with openCV
        self.namePhoto = fileName[0]
        self.imageInMemory = cv2.imread(self.namePhoto, 1)
        self.imageInMemory = cv2.cvtColor(self.imageInMemory, cv2.COLOR_BGR2RGB)

        # Convert cvMat to QImage
        qImage = QImage(self.imageInMemory.data,self.imageInMemory.shape[1],self.imageInMemory.shape[0], self.imageInMemory.strides[0], QImage.Format_RGB888)

        # Convert QImage to pixmap
        qImagePixmap = QPixmap.fromImage(qImage)

        self.photo = QPixmap(qImagePixmap)

        self.w = self.labelImage.width()
        self.h = self.labelImage.height()
        self.imageScaled = self.photo.scaled(self.w,self.h, Qt.KeepAspectRatio)
        self.labelImage.setPixmap(self.imageScaled)
        self.labelImage.show()



if __name__ == '__main__':
    appWebCam = QApplication(sys.argv)
    ex = AplicationWebCam()
    sys.exit(appWebCam.exec_())
