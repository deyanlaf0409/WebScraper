import json
import re
from Library.book import Book

# dictionary to convert from written format to integer
RATING_NUMS = {
            "Zero": 0,
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
        }


def helper_filter(number, attr_to_filter_through):
    """
    This function helps to parse filters from the command line.
    :param number: the scraped numeric data to compare to the filter.
    :param attr_to_filter_through: The requested filter by the user.
    :return: False if there is an error, also if the requested filter does not match the scraped data.
    True if everything is all right.
    """
    pattern = r"[0-9.]+"
    num_after_pattern = float(re.findall(pattern, attr_to_filter_through)[0])
    if ">" in attr_to_filter_through:
        if num_after_pattern > number:
            return False
    elif "<" in attr_to_filter_through:
        if num_after_pattern < number:
            return False
    else:
        if num_after_pattern != number:
            return False

    return True


class Filter:

    def __init__(self, num_of_books=1000, genres=None, price_filter="",
                 upc_filter=None, availability_filter=None, rating_filter=str(" "),
                 words_in_title=None, words_in_description=None, num_of_reviews=None):
        """
                Constructs all the neccessary attributes for the scraper object
                :param num_of_books: Number of book that has to be scraped
                :param genres: Genres that has to be scraped
                :param filters: Filter we can use to scrape
                :param words_in_title: Filter to search by words in the title
                :param words_in_description: Search by passed words in description of the book
                """

        self.num_of_books = num_of_books
        self.genres = genres if genres is not None else []
        self.price_filter = price_filter.replace(" ", "")
        self.upc_filter = upc_filter
        self.availability_filter = availability_filter
        self.rating_filter = rating_filter.replace(" ", "")
        self.words_in_title = words_in_title.split() if words_in_title is not None else []  # gotovo
        self.words_in_description = words_in_description if words_in_description is not None else []
        self.num_of_reviews = num_of_reviews

    def __filter_by_upc(self, upc):
        """
        This method fulters by UPC.
        :param upc: the scraped UPC data.
        :return: True if it is a match to the requested UPC, false if not.
        """
        return False if upc not in self.upc_filter else True

    def __search_in_title(self, scraped_title):
        """
        This method searches for books by given titles.
        :param scraped_title: The title of the currently scraped book.
        :return: True if there is a match, False if not.
        """
        words_in_title = self.words_in_title if isinstance(self.words_in_title, unicode)\
            else self.words_in_title[0]
        with open(words_in_title, "r") as user_input:
            valid_titles = json.load(user_input)
            if scraped_title in valid_titles:
                valid_titles.remove(scraped_title)
                return True
            else:
                return False

    def __search_by_words_in_desc(self, scraped_desc):
        """
        This method search by words in given book description.
        :param scraped_desc: Passed book description
        :return: False if some of the words are not in the description, else returns True
        """
        for word in self.words_in_description.split(","):
            if word not in scraped_desc:
                return False

        return True

    def main_filter(self, bs4_book):
        """
        This method is the main filter method. It is dynamically scraping the webpage according to the requested
        filters from the command line.
        :param bs4_book: The parsed HTML data of a book's webpage.
        :return: Book object if the scraped book matches all the requested filters. False if there is a non-matching criteria.
        """
        book = Book()
        if self.price_filter:
            price = float(bs4_book.find("p", class_="price_color").text[2:])
            if not helper_filter(price, self.price_filter): return False
            else: book.price = price
        if self.rating_filter:
            rating = int(RATING_NUMS[bs4_book.find("p", class_="star-rating")["class"][1]])
            if not helper_filter(rating, self.rating_filter): return False
            else: book.rating = rating
        if self.upc_filter:
            upc = bs4_book.find_all("th")[0].find_next().text
            if not self.__filter_by_upc(upc): return False
            else: book.upc = upc
        if self.availability_filter:
            temp = bs4_book.find("p", class_="availability").text.strip()
            num_as_string = re.findall(r"[0-9]+", temp)
            availability = int(num_as_string[0])
            if not helper_filter(availability, self.availability_filter): return False
            else: book.availability = availability
        if self.num_of_reviews:
            num_of_reviews = int(bs4_book.find_all("th")[6].find_next().text)
            if not helper_filter(num_of_reviews, self.num_of_reviews): return False
            else: book.num_of_reviews = num_of_reviews
        if self.words_in_description:
            try:
                description = bs4_book.find("p", class_=None).text.strip().encode('ascii', 'ignore').decode()
            except:
                description = ""
            if not self.__search_by_words_in_desc(description): return False
            else: book.description = description
        if self.words_in_title:
            name = bs4_book.find("h1").text
            if not self.__search_in_title(name): return False
            else: book.name = name

        return book
