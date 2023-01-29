class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


dan1 = Rectangle(11, 22)
print(dan1.get_area())
