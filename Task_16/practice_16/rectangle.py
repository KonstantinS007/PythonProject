class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeigth(self):
        return self.height

# Метод рачитывающий площадь
    def getArea(self):
        return self.width * self.height
