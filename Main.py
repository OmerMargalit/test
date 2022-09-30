from Circle import Circule
from SHAPES import *
from Rectangle import *
from Square import *
from Circle import *
from ShapesStack import *


def main():

    s = Shapse("BLACK")
    print(s)
    rectangle = Rectangle("RED", 3, 2)
    print(rectangle)
    square = Square("BLUE", 3)
    print(square)
    circule = Circule("PINK", 4)
    print(circule)
    print(square.ShapesConnecting(rectangle))
    my_container = shapesstack()
    my_container.generate(100)
    print("total area:", my_container.sumAreas())
    print("total perimeter:", my_container.sumPerimteres())
    print("colors:", my_container.countColors())


if __name__ == "__main__":
    main()

