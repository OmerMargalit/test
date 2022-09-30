from SHAPES import *

class Rectangle(Shapse):

    def __init__(self, color="Black", x=1, y=2):
        super().__init__(color, (x*y), (x*2)+(y*2))
        self.length = x
        self.width = y

    def ShapesConnecting(self, rect):
        """
        :param rect: the shape
        :return: return the new width and length of the shape
        """
        if isinstance(rect, Rectangle):
            self.rect_width = rect.get_width()
            self.rect_length = rect.get_length()
            self.new_width = self.width + self.rect_width
            self.new_length = self.length + self.rect_length
            return "New Width: " + str(self.new_length*self.new_width) + " ,New Lingth: " + str((self.new_length*2)+(self.new_width*2))


    def get_length(self):
        """
        :return: return length
        """
        return self.length

    def get_width(self):
        """
        :return: return width
        """
        return self.width

    def __str__(self):
        return super().__str__() + " length:" + str(self.length) + " ,width:" + str(self.width)