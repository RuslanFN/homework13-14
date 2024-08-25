from typing import Union
class BookNotFoundError(Exception):
    def __init__(self,title = '', *args: object) -> None:
        super().__init__('такой книги нет: ' + str(title), *args)
    
class Library():
    def __init__(self) -> None:
        self.__books = []

    def add_book(self, title: str):

        self.__books.append(title)

    def remove_book(self, title: str):
        """ Удаляет книгу из списка по её названию
            или вызывает исключение BookNotFoundError
        """
        try:
            self.__books.remove(title)
        except ValueError:
            raise BookNotFoundError
        
    def list_books(self):
        return self.__books
    



