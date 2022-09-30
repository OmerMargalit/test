from SHAPES import *
import math


class Circule(Shapse):

    def __init__(self, color="Blue", r=1):
        super().__init__(color, (r**2) * math.pi, 2 * r * math.pi)
        self.r = r