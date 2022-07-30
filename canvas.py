import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.background = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.background[:] = [self.color]

    def make(self):
        img = Image.fromarray(self.background)
        img.save("canvas.png")
