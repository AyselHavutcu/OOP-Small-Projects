from PIL import Image

import numpy as np


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    #create a 3D array of zeros
    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)