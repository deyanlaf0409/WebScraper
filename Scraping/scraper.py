import re
from bs4 import BeautifulSoup
import requests
from Library.book import Book
from urlparse import urljoin
from Link_Builder.website import WebSite
from Link_Builder.linkbuilder import LinkBuilder
from Arg_Parser.arg_parser import Arg_Parser
from Filter.Filter import Filter

# This is the default link when there are no categories from input
WITHOUT_CATEGORY = "https://books.toscrape.com/catalogue/page-1.html"

# This is a dictionary that helps convert word representation of nubmers to integers.
RATING_NUMS = {
    "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def fill_book(bs4_book, book_object):
    """
    This method scrapes a given book's webpage and fills our book object with the scraped data.
    :param bs4_book: The book's wepbage parsed by beautiful soup.
    :param book_object: The current book object to fill.
    :return: The book object with filled data.
    """
    if not book_object.name:
        name = bs4_book.find("h1").text
        book_object.name = name
    if not book_object.rating:
        rating = int(RATING_NUMS[bs4_book.find("p", class_="star-rating")["class"][1]])
        book_object.rating = rating
    if not book_object.upc:
        upc = bs4_book.find_all("th")[0].find_next().text
        book_object.upc = upc
    if not book_object.description:
        try:
            description = bs4_book.find("p", class_=None).text.strip().encode('ascii', 'ignore').decode()
        except:
            description = ""
        book_object.description = description
    if not book_object.price:
        price = float(bs4_book.find("p", class_="price_color").text[2:])
        book_object.price = price
    if not book_object.availability:
        temp = bs4_book.find("p", class_="availability").text.strip()
        num_as_string = re.findall(r"[0-9]+", temp)
        availability = int(num_as_string[0])
        book_object.availability = availability
    if not book_object.num_of_reviews:
        num_of_reviews = int(bs4_book.find_all("th")[6].find_next().text)
        book_object.num_of_reviews = num_of_reviews
    return book_object


class Scraper:
    """
    This is our scraper class that is responsible for scraping books according to flags set by the user.
    """
    def __init__(self, filter=None):
        if filter is not None:
            if filter.num_of_books == "gui premature exit": quit()
        if filter is None:
            cmd_args = Arg_Parser()
            self.filter = Filter(cmd_args.num_of_books, genres=cmd_args.list_of_genres,
                            rating_filter=cmd_args.rating, availability_filter=cmd_args.availability,
                            upc_filter=cmd_args.upc, price_filter=cmd_args.price,
                            words_in_description=cmd_args.list_of_keywords,
                            words_in_title=cmd_args.list_of_titles,
                            num_of_reviews=cmd_args.num_of_reviews)
        else:
            self.filter = filter

    def get_books_info(self):
        """
        get_book_info is a public method that makes use of _create_category and _book_page_urls in order to scrape
        the site according to params set by our user. It creates a list of Book objects that contains info about them.
        :return: list of Book objects
        """
        list_of_books = []
        link_builder = LinkBuilder()
        for category in link_builder.get_category(self.filter.genres):
            while True:
                for book in link_builder.get_book(category.bs4_object):
                    bs4_book = BeautifulSoup(requests.get(urljoin(link_builder.url, "/catalogue" + book)).text, "html.parser")
                    book_object = self.filter.main_filter(bs4_book)
                    if book_object: list_of_books.append(fill_book(bs4_book, book_object))
                    else: continue
                    if len(list_of_books) == self.filter.num_of_books: return list_of_books
                try:
                    next_page = category.bs4_object.find("li", {"class": "next"}).find("a")["href"]

                except:
                    next_page = None

                if next_page:
                    category = WebSite(urljoin(category.base_url, next_page))
                else:
                    break

        return list_of_books

