class Sorter:
    """
    A sorter class that sorts books according to user input.
    """
    def __init__(self, book_filter=None, order=""):
        if not book_filter:
            self.filter = []
        self.filter = book_filter
        self.order = order

    def sort_books(self, books):
        """
        This method sorts a given list of scraped book objects.
        :param books: List of book objects that we scraped.
        :return: Sorted list according to the user input.
        """
        order = ("ascending", "descending")
        if self.filter[-1] in order: self.filter.pop()
        if not self.filter: return books
        return sorted(books, key=lambda d: tuple(d.__dict__[item] for item in self.filter),
                      reverse=True if self.order == "descending" else False)
