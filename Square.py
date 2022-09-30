from Rectangle import *

class Square(Rectangle):

    def __init__(self, color="Black", x=1):
        super().__init__(color, x, x)
        self.x = x

    def get_x(self):
        """
        :return: return the size of the square sides
        """
        return self.x
