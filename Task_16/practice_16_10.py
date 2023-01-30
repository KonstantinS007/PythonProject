class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')


rec1 = Square(0)

