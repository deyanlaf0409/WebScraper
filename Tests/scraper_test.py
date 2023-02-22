# coding=utf-8
import unittest
from Library.book import Book
from bs4 import BeautifulSoup
from Scraping.scraper import *
from Filter.Filter import Filter
import re
import requests


class TestFillBook(unittest.TestCase):
    def setUp(self):
        test_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

        self.bs4_book = BeautifulSoup(requests.get(test_url).text, "html.parser")
        self.filter = Filter(num_of_books=1)
        self.scraper = Scraper(self.filter)
        self.book_object = Book()

    def test_fill_book_name(self):
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(self.book_object.name, "A Light in the Attic")

    def test_fill_book_rating(self):
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(self.book_object.rating, 3)

    def test_fill_book_upc(self):
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(self.book_object.upc, "a897fe39b1053632")

    def test_fill_book_description(self):
        test_description = "It's hard to imagine a world without A Light in the Attic. This now-classic collection of " \
                           "poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special " \
                           "edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. " \
                           "Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh " \
                           "and smile and love th It's hard to imagine a world without A Light in the Attic. This " \
                           "now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th " \
                           "anniversary with this special edition. Silverstein's humorous and creative verse can amuse " \
                           "the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these " \
                           "rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? " \
                           "RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?" \
                           "And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in " \
                           "for you. Shel, you never sounded so good. ...more"
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(test_description, self.book_object.description)

    def test_fill_book_price(self):
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(self.book_object.price, 51.77)

    def test_fill_book_availability(self):
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(self.book_object.availability, 22)

    def test_fill_book_num_of_reviews(self):
        fill_book(self.bs4_book, self.book_object)
        self.assertEqual(self.book_object.num_of_reviews, 0)


class TestBookScrapper(unittest.TestCase):  # test get_books_info

    def setUp(self):
        self.filter = Filter(num_of_books=1)
        self.scraper = Scraper(self.filter)
        self.scrapper = Scraper(self.filter)  # assuming BookScrapper is the class that contains get_books_info method

    def test_get_books_info(self):
        # possible scraping of entire website
        books = self.scrapper.get_books_info()
        self.assertGreaterEqual(len(books), 1)  # Ensure that at least one book is returned
        for book in books:
            self.assertIsNotNone(book.name)  # Ensure that each book object has a name
            self.assertIsNotNone(book.rating)  # Ensure that each book object has a rating
            self.assertIsNotNone(book.upc)  # Ensure that each book object has a upc
            self.assertIsNotNone(book.description)  # Ensure that each book object has a description
            self.assertIsNotNone(book.price)  # Ensure that each book object has a price
            self.assertIsNotNone(book.availability)  # Ensure that each book object has an availability
            self.assertIsNotNone(book.num_of_reviews)  # Ensure that each book object has a number of reviews

