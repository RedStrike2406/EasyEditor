import os

from PIL import Image, ImageFilter

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.fileName = None
        self.dir = None
        self.dir_save = 'Modified'

    def loadImage(self, dir, filename):
        self.dir = dir
        self.fileName = filename
        pathImage = os.path.join(dir, filename)
        self.image = Image.open(pathImage)
    
    def saveImage(self):
        pathDirSave = os.path.join(self.dir, self.dir_save)
        if not (os.path.exists(pathDirSave) or os.path.isdir(pathDirSave)):
            os.mkdir(pathDirSave)
        
        pathImageSave = os.path.join(pathDirSave,  self.fileName)
        self.image.save(pathImageSave)

    
    def do_blackWhite(self):
        if self.image:
            self.image = self.image.convert("L")
            self.saveImage()

            pathImageSave = os.path.join(self.dir,  self.dir_save, self.fileName)

            return(pathImageSave)
        
    def do_left(self):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()

            pathImageSave = os.path.join(self.dir,  self.dir_save, self.fileName)

            return(pathImageSave)

    def do_right(self):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()

            pathImageSave = os.path.join(self.dir,  self.dir_save, self.fileName)

            return(pathImageSave)
    
    def do_flip(self):
        if self.image:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()

            pathImageSave = os.path.join(self.dir,  self.dir_save, self.fileName)

            return(pathImageSave)
    
    def do_sharpen(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.saveImage()

            pathImageSave = os.path.join(self.dir,  self.dir_save, self.fileName)

            return(pathImageSave)