from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QFileDialog)
from PyQt5.QtGui import (QPixmap)
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow
from imageprocessor import ImageProcessor

import os


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_events()

        self.workDir = None
        self.saveDir = None

        self.reworkImage = ImageProcessor()

        self.show()

    def connect_events(self):
        self.ui.pb_folder.clicked.connect(self.showListFilename)
        self.ui.pb_save.clicked.connect(self.choseSaveFile)
        self.ui.lw_pict.itemClicked.connect(self.showChoicenImage)
        self.ui.pb_BlackWhite.clicked.connect(self.do_blackWhite)
        self.ui.pb_left.clicked.connect(self.do_left)
        self.ui.pb_right.clicked.connect(self.do_right)
        self.ui.pb_mirror.clicked.connect(self.do_flip)
        self.ui.pb_sharpen.clicked.connect(self.do_sharpen)

    def choiceFolder(self):
        workDir = QFileDialog.getExistingDirectory()
        return workDir

    def choseSaveFile(self):
        #pathFile, _ = QFileDialog.getSaveFileName(self, "Зберегти файл як")
        # pathImage = self.reworkImage.saveImage()
        pathImage = self.reworkImage.saveImage()
    
    def showListFilename(self):
        extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        self.workDir = self.choiceFolder()
        if self.workDir:
            filenames = os.listdir(self.workDir)
            filteredFilenames = self.filter(filenames, extensions)
            self.ui.lw_pict.clear()
            self.ui.lw_pict.addItems(filteredFilenames)
    

    def filter(self, filenames, extensions):
        filteredFilenames = []
        for filename in filenames:
            for extension in extensions:
                if filename.endswith(extension):
                        filteredFilenames.append(filename)
        return(filteredFilenames)
    

    def showChoicenImage(self):
        filename = self.ui.lw_pict.currentItem().text()
        pathImage = os.path.join(self.workDir, filename)
        self.showImage(pathImage)
        
        self.reworkImage.loadImage(self.workDir, filename)


    def showImage(self, path):
        if path:
            pixmap = QPixmap(path)
            w, h = self.ui.l_picture.width(), self.ui.l_picture.height()
            pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
            self.ui.l_picture.setPixmap(pixmap)

    def do_blackWhite(self):
        pathImage = self.reworkImage.do_blackWhite()
        self.showImage(pathImage)
    
    def do_left(self):
        pathImage = self.reworkImage.do_left()
        self.showImage(pathImage)
    
    def do_right(self):
        pathImage = self.reworkImage.do_right()
        self.showImage(pathImage)
    
    def do_flip(self):
        pathImage = self.reworkImage.do_flip()
        self.showImage(pathImage)
    
    def do_sharpen(self):
        pathImage = self.reworkImage.do_sharpen()
        self.showImage(pathImage)
    
    






if __name__ == "__main__":
    import sys


    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

