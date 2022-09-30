from SHAPES import *
import random
from Rectangle import *
from Square import *
from Circle import *
Color_list = ["RED", "BLUE", "YELLOW", "BLACK", "GREEN"]
class shapesstack:

    def __init__(self):
        self.shapes_list = list()

    def generate(self, x):
        """
        :param x: number of shapses to generate
        :return: return  the shape with color and sizes
        """
        for i in range(x):
            number = random.randint(1, 3)
            if number == 1:
                shape_color = random.randint(0, 4)
                new_color = Color_list[shape_color]
                width = random.randint(1, 9)
                length = random.randint(1, 9)
                while width == length:
                    length = random.randint(1, 9)
                self.shapes_list.append(Rectangle(new_color, width, length))

            elif number == 2:
                shape_color = random.randint(0, 4)
                new_color = Color_list[shape_color]
                width = random.randint(1, 9)
                self.shapes_list.append(Square(new_color, width))

            elif number == 3:
                shape_color = random.randint(0, 4)
                new_color = Color_list[shape_color]
                radios = random.randint(1, 9)
                self.shapes_list.append(Circule(new_color, radios))

    def sumAreas(self):
        """
        :return: return the area of all the shapes that generate
        """
        sum = 0
        for shape in self.shapes_list:
            sum += shape.get_area()
        return sum

    def sumPerimteres(self):
        """
        :return: return the sum of all the shapes that generate
        """
        perimteres = 0
        for shape in self.shapes_list:
            perimteres += shape.get_hekaf()
        return perimteres

    def countColors(self):
        """
        :return: return a dictionarie of colors and how many times each color has been drawn
        """
        red = 0
        blue = 0
        yellow = 0
        black = 0
        green = 0
        for color in self.shapes_list:
            if color.get_color() == "RED":
                red = red + 1

            if color.get_color() == "BLUE":
                blue = blue + 1

            if color.get_color() == "YELLOW":
                yellow = yellow + 1

            if color.get_color() == "BLACK":
                black = black + 1

            if color.get_color() == "GREEN":
                green = green + 1

        color_dictionarie = {"RED": red, "BLUE": blue, "YELLOW": yellow, "BLACK": black, "GREEN": green}
        return color_dictionarie