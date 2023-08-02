# Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

class Rectangle:
    """The class contains a description of the rectangle and various operations with it"""
    def __init__(self, a, b=None):
        if b == None:
            b = a
        if a < b:
            a, b = b, a    
        self.a = a
        self.b = b

    def perimeter(self):
        """Calculating the perimeter of a rectangle"""
        return (self.a + self.b) * 2

    def sq(self):
        """Calculating the area of a rectangle"""
        return self.a * self.b
    
    def __add__(self, other):
        """Adding rectangles"""
        c = self.a + other.a
        d = self.b + other.b
        return Rectangle(c, d)

    def __sub__(self, other):
        """Subtracting rectangles"""
        p1 = 2 * (self.a + self.b)
        p2 = 2 * (other.a + other.b)
        if p1 > p2 :
            c = self.a - other.a
            d = self.b - other.b
        else:
            c = other.a - self.a
            d = other.b - self.b
        return Rectangle(c,d)
    
    def __str__(self):
        return f'{self.a}x{self.b}'


rec = Rectangle(10, 5)
# print('Сторона a = ', rec.a)
# print('Сторона b = ', rec.b)
# print('Периметр = ', rec.perimeter())
# print('Площадь = ', rec.sq())
pr1 = Rectangle(3, 7)
pr2 = Rectangle(5, 2)
print("Первый прямоугольник: ", pr1)
print("Первый прямоугольник: ", pr2)
print("Результат вычитания и сложения:", pr1-pr2, pr1+pr2)