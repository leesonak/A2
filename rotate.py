import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import qimage2ndarray
import numpy as np
from PyQt5.QtCore import Qt
basic_ui = uic.loadUiType("rotate.ui")[0]
class WindowClass(QMainWindow, basic_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : self.Imageshow())
        self.pushButton_2.clicked.connect(lambda : self.rotate_pixmap())

    def Imageshow(self):
        fileName,_=QFileDialog.getOpenFileName(self,"Open File",".")

        image = QImage(fileName)

        if image.isNull():
            QMessageBox.information(self,"Image Viewer","Cannot load %s" %fileName)
            return

        qPixmapVar = QPixmap.fromImage(image)
        qPixmapVar = qPixmapVar.scaled(400,400,Qt.KeepAspectRatioByExpanding)
        self.label.setPixmap(qPixmapVar)
            

        self.show()
            
    def rotate_pixmap(self):
        image=self.label.pixmap()
        self.image = QImage(image)
        if self.image.isNull():
            QMessageBox.information(self,"Image Viewer","Cannot load %s" %image)
            return

        image_array = qimage2ndarray.rgb_view(self.image)
        image_array = np.flip(image_array,0)
        self.image = qimage2ndarray.array2qimage(image_array,normalize=False)
        qPixmapVar = QPixmap.fromImage(self.image)
        qPixmapVar = qPixmapVar.scaled(400,400,Qt.KeepAspectRatioByExpanding)
        self.label.setPixmap(qPixmapVar)
        
if __name__ == "__main__" :
    app= QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
