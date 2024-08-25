import unittest
import task13_2

class TestTask13_2(unittest.TestCase):
    def setUp(self) -> None:
        self.library = task13_2.Library()
    
    def test_add_book(self):
        self.library.add_book('Война и мир')
        self.assertEqual(['Война и мир'], self.library.list_books())
    
    def test_remove_book(self):
        self.library.add_book('Война и мир')
        self.library.add_book('Буратино')
        self.library.remove_book('Буратино')
        self.assertEqual(['Война и мир'], self.library.list_books())
        self.assertRaises(task13_2.BookNotFoundError, self.library.remove_book, ('Буратино'))
        
    def test_list_books(self):
        self.library.add_book('Конституция РФ')
        self.library.add_book('Муму')
        self.library.remove_book('Муму')
        self.library.add_book('Уроки программирования')
        self.assertEqual(['Конституция РФ', 'Уроки программирования'], self.library.list_books())

if __name__ == '__main__':
    unittest.main()