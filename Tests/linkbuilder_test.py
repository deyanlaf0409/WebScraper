import unittest
from bs4 import BeautifulSoup
from Link_Builder.linkbuilder import LinkBuilder
from Link_Builder.website import WebSite
import requests

FIND_CATEGORY = "http://books.toscrape.com/catalogue/category/books_1/index.html"

linkbuilder = Linkbuilder = LinkBuilder()


class TestGetCategory(unittest.TestCase):

    url = "http://books.toscrape.com"
    _with_category = "http://books.toscrape.com/catalogue/category"
    _without_category = "https://books.toscrape.com/catalogue/page-1.html"
    _bs4_find_category = BeautifulSoup(requests.get(FIND_CATEGORY).text, "html.parser")

    def test_get_category(self):
        # Create a sample page with categories

        # Call the get_category method with one category
        categories = ["Travel", "random nonexistant category"]
        return_list = linkbuilder.get_category(categories)

        # Check if the return_list is correct
        expected_list = [WebSite(self._with_category + "/books/travel_2/index.html")]
        self.assertEqual(return_list[0].base_url, expected_list[0].base_url)

        self.assertNotEqual(categories, return_list)

        return_list = linkbuilder.get_category([])
        expected_result = "https://books.toscrape.com/catalogue/page-1.html"
        self.assertEqual(return_list[0].base_url, expected_result)


class TestGetBook(unittest.TestCase):

    def test_get_book(self):
        # Create a sample page
        page_html = '<html><body><h3>../../../Book 1</h3><a href="book1.html">Book 1 Link</a><h3>Book 2</h3>' \
                    '<a href="book2.html">Book 2 Link</a></body></html>' #tests for both ways hrefs could occur
        page = BeautifulSoup(page_html, 'html.parser')

        # Call the get_book method
        return_list = linkbuilder.get_book(page)

        # Check if the return_list is correct
        expected_list = ['/book1.html', '/book2.html']
        self.assertEqual(return_list, expected_list)

