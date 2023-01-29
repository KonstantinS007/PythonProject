from rectangle import Rectangle, Square, Circle
# создаем два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# выводим площади двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

# создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)

# выводим площади двух квадратов
print(square_1.get_area_square(), square_2.get_area_square())

# создаем два круга
circle_1 = Circle(10)
circle_2 = Circle(12)

# выводим площади двух кругов
print(circle_1.get_area_circle(), circle_2.get_area_circle())

# создаем класс фигуры
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
