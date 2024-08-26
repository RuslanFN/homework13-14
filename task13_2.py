from typing import Union
from logger import Logger
import argparse

argparser = argparse.ArgumentParser(description='Программа имитирующая работу библиотеки. Вы можете передать параметры для запуска -books')

argparser.add_argument('-books', type=str, nargs='+', help='список книг через пробел')
logger = Logger('Library')

class BookNotFoundError(Exception):
    def __init__(self,title = '', *args: object) -> None:
        super().__init__('такой книги нет: ' + str(title), *args)
    
class Library():
    def __init__(self) -> None:
        if argparser.parse_args().books:
            self.__books = argparser.parse_args().books
        else:
            self.__books = []
        logger.log_info('Инициализация')

    def add_book(self, title: str):
        self.__books.append(title)
        logger.log_info(f'Добавил книгу {title}')

    def remove_book(self, title: str):
        """ Удаляет книгу из списка по её названию
            или вызывает исключение BookNotFoundError
        """
        try:
            self.__books.remove(title)
            logger.log_info(f'Удалил книгу {title}')
        except ValueError:
            logger.log_warning(f'Книга {title} не найдена')
            raise BookNotFoundError
        
    def list_books(self):
        logger.log_info(f'Вернул список книг {self.__books}')
        return self.__books
    
if __name__ == '__main__':
    lib = Library()
    lib.add_book('Война и мир')
    lib.add_book('Буратино')
    lib.list_books()
    lib.remove_book('Буратино')
    lib.remove_book('Буратино')


