import unittest
from Library.book import Book
from Sorting.sorting import Sorter

sorter = Sorter()

#
# self.name = name
#         self.rating = rating
#         self.upc = upc
#         self.description = description
#         self.price = price
#         self.availability = availability
#         self.num_of_reviews = num_of_reviews


class TestSortBooks(unittest.TestCase):
    def setUp(self):
        self.books = [
            Book("A", rating=1, upc="1111", description="a", price=1.00, availability=1, num_of_reviews=1),
            Book("B", rating = 2, upc="2222", description= "b", price=2.00, availability=2, num_of_reviews=2),
            Book("C", rating=3, upc="3333", description="c", price=3.00, availability=3, num_of_reviews=3),
            Book("D", rating=4, upc="4444", description="d", price=4.00, availability=4, num_of_reviews=4),
        ]

        self.expected_ascending = [
            self.books[0],  # A
            self.books[1],  # B
            self.books[2],  # C
            self.books[3],  # D
        ]
        self.expected_descending = [
            self.books[3],  # D
            self.books[2],  # C
            self.books[1],  # B
            self.books[0],  # A
        ]

    def test_sort_ascending_by_title(self):
        filter = ["name"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_title(self):
        filter = ["name"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

    def test_sort_ascending_by_rating(self):
        filter = ["rating"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_rating(self):
        filter = ["rating"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

    def test_sort_ascending_by_upc(self):
        filter = ["upc"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_upc(self):
        filter = ["upc"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

    def test_sort_ascending_by_description(self):
        filter = ["description"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_description(self):
        filter = ["description"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

    def test_sort_ascending_by_price(self):
        filter = ["price"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_price(self):
        filter = ["price"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

    def test_sort_ascending_by_availability(self):
        filter = ["availability"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_availability(self):
        filter = ["availability"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

    def test_sort_ascending_by_num_of_reviews(self):
        filter = ["num_of_reviews"]
        order = "ascending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_ascending)

    def test_sort_descending_by_num_of_reviews(self):
        filter = ["num_of_reviews"]
        order = "descending"
        sorter.filter = filter
        sorter.order = order
        sorted_books = sorter.sort_books(self.books)
        self.assertEqual(sorted_books, self.expected_descending)

