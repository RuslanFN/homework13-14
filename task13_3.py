class Rectangle:
    def __init__(self, width: tuple[int, float], height: tuple[int, float]) -> None:
        '''
        инициализация прямоугольника
        >>> r = Rectangle(3, 4)
        >>> r.get_area()
        12
        >>> r.get_perimetr()
        14
        >>> r = Rectangle(-7, -2)
        Traceback (most recent call last):
        ...
        ValueError
        >>> r = Rectangle(0, 0)
        Traceback (most recent call last):
        ...
        ValueError
        '''
        if width <= 0:
            raise ValueError
        if height <= 0:
            raise ValueError
        self.width = width
        self.height = height

    def set_dimension(self, width: tuple[int, float], height: tuple[int, float]) -> None:
        '''
        Установка новых длины и ширины
        >>> r = Rectangle(4, 4)
        >>> r.get_perimetr()
        16
        >>> r.get_area()
        16
        >>> r.set_dimension(3, 3)
        >>> r.get_area()
        9
        >>> r.get_perimetr()
        12
        >>> r.set_dimension(0, 0)
        Traceback (most recent call last):
        ...
        ValueError
        >>> r.set_dimension(-8, -3)
        Traceback (most recent call last):
        ...
        ValueError
        '''
        
        if width <= 0:
            raise ValueError
        if height <= 0:
            raise ValueError

        self.width = width
        self.height = height

    def get_area(self) -> tuple[int, float]:
        '''
        метод возвраающий площадь прямоугольника
        >>> r = Rectangle(2, 3)
        >>> r.get_area()
        6
        '''
        return self.width*self.height
    
    def get_perimetr(self) -> tuple[int, float]:
        '''
        метод возвраающий периметр прямоугольника
        >>> r = Rectangle(2, 3)
        >>> r.get_perimetr()
        10
        '''
        return (self.height + self.width) * 2

#Rectangle(-2, -2)
import doctest
if __name__ == '__main__':
    doctest.testmod()