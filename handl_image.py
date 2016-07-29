# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
import json


class HandlImage(object):

    def __init__(self, path):
        self.image = Image.open(path) #Открываем изображение.
        self.draw = ImageDraw.Draw(self.image) #Создаем инструмент для рисования.
        self.width = self.image.size[0] #Определяем ширину.
        self.height = self.image.size[1] #Определяем высоту.
        self.pix = self.image.load() #Выгружаем значения пикселей.


    def change_size(self,down_path,size):
        """size is tuple, ex (64,64)
        """

        img = self.image.resize(size,Image.ANTIALIAS)
        img.save(down_path, "JPEG")


    def convert(self,obj):
        """It's convert binary object in 'latin-1'.
        Support, the utf-8 is not working"""

        if isinstance(obj, bytes):
            return obj.decode('latin-1')
        return obj


    def get_exif_data(self):
        """EXIF data contains binary data, it is necessary to convert binary data to latin1 due to
        json incompatibility. see http://stackoverflow.com/questions/22621143/serializing-binary-data-in-python
        for more details"""
        exif_data = self.image._getexif()
        decoded_exif = dict(map(lambda t: (self.convert(t[0]), self.convert(t[1])), exif_data.items()))
        return json.dumps(decoded_exif)
        #return decoded_exif


if __name__ == '__main__':
    path = os.path.abspath('./test_im')
    full_path = os.path.join(path, '2.JPG')
    down_path = os.path.join(path, '2_news.JPG')

    im = HandlImage(full_path)
    print (im.get_exif_data())
    im.change_size(down_path,(64,64))

