import requests
from bs4 import BeautifulSoup
from Link_Builder.website import WebSite

FIND_CATEGORY = "http://books.toscrape.com/catalogue/category/books_1/index.html"

class LinkBuilder:
    """
    This is the link builder class, which is generating dynamic links according to program needs.
    """
    url = "http://books.toscrape.com"
    _with_category = "http://books.toscrape.com/catalogue/category"
    _without_category = "https://books.toscrape.com/catalogue/page-1.html"
    _bs4_find_category = BeautifulSoup(requests.get(FIND_CATEGORY).text, "html.parser")

    def get_category(self, categories=None):
        """
        This method gets a category from the user input. If there are no categories it goes by default.
        :param categories: Default None, otherwise takes user inputted categories.
        :return: parsed list of categories.
        """
        if not categories: return [WebSite(self._without_category)]

        list_of_categories = []
        tag = self._bs4_find_category.find_all("a", href=True)
        for category in categories:
            for check_against_category in tag:
                genre_link = check_against_category.get("href")[2:]
                if genre_link[0] == '/':
                    if check_against_category.text.strip().lower() == category.lower():
                        list_of_categories.append(WebSite(self._with_category + genre_link))
                        break

        return list_of_categories

    def get_book(self, page):
        """
        This method generates an individual book link from a given page.
        :param page: The current page.
        :return: list of links for all the books on the current page.
        """
        return_list = []
        books = page.find_all("h3")
        for book in books:
            book = book.find_next()
            return_list.append(book["href"][8:] if book["href"][0] == '.' else '/' + book["href"])
        return return_list
