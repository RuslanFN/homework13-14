from logger import Logger

import argparse

argparser = argparse.ArgumentParser(description='Программа имитирующая операции над прямоугольником. Вы можете передать параметры для запуска -width -height')

argparser.add_argument('-width', type=float, help='параметр ширины')
argparser.add_argument('-height', type=float, help='параметр длины')
logger = Logger('Rectangle')




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
        >>> r = Rectangle('1', '1')
        Traceback (most recent call last):
        ...
        TypeError
        '''
        
        if type(width) not in (int, float) or type(height) not in (int, float):
            logger.log_warning('Ошибка типа данных в методе init')
            raise TypeError
        if width <= 0:
            logger.log_warning('Значение меньше нуля в методе init')
            raise ValueError
        if height <= 0:
            logger.log_warning('Значение меньше нуля в методе init')
            raise ValueError
        self.width = width
        self.height = height
        logger.log_info(f'Инициализация прямоугольника {width} {height}')
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
        >>> r.set_dimension('8', '3')
        Traceback (most recent call last):
        ...
        TypeError
        '''
        if type(width) not in (int, float) or type(height) not in (int, float):
            logger.log_warning('Ошибка типа данных в методе set_dimension')
            raise TypeError
        if width <= 0:
            logger.log_warning('Значение меньше нуля в методе set_dimension')
            raise ValueError
        if height <= 0:
            logger.log_warning('Значение меньше нуля в методе set_dimension')
            raise ValueError
        self.width = width
        self.height = height
        logger.log_info(f'Установка новых значений длины и ширины {width} {height}')

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
if __name__ == '__main__':
    if argparser.parse_args().width and argparser.parse_args().height:
        width = argparser.parse_args().width
        height = argparser.parse_args().height
        rec = Rectangle(width, height)
    else:
        rec = Rectangle(2, 2)
    rec.set_dimension(-3, -2)
    print(rec.get_area())
    print(rec.get_perimetr())

#import doctest
#if __name__ == '__main__':
    #doctest.testmod()