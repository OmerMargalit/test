class Shapse:

    def __init__(self, color="Red", area=1, hekaf=1):
        self.color = color
        self.area = area
        self.hekaf = hekaf

    def get_area(self):
        """
        :return: return area
        """
        return self.area

    def get_hekaf(self):
        """
        :return: return hekaf
        """
        return self.hekaf

    def get_color(self):
        """
        :return: return color
        """
        return self.color

    def set_color(self, color):
        """
        update the color
        """
        self.color = color
        return "Color:" + self.color

    def __str__(self):
        return "color:" + str(self.color) + " ,area:" + str(self.area) + " ,hekef:" + str(self.hekaf)