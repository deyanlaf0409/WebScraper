class Book:
    """
    Blueprint for scraped books information
    """

    def __init__(self, name=None, rating=None, upc=None, description=None
                 , price=None, availability=None, num_of_reviews=None):
        self.name = name
        self.rating = rating
        self.upc = upc
        self.description = description
        self.price = price
        self.availability = availability
        self.num_of_reviews = num_of_reviews

    def __str__(self):
        """
        This is the string representation of our book.
        :return: Pretty string.
        """
        return "Name: {0}\n" \
               "Rating: {1}\n" \
               "UPC: {2}\n" \
               "Description: {3}\n" \
               "Price: {4}\n" \
               "Availability: {5}\n" \
               "Number of Reviews: {6}\n".format(self.name.encode('ascii', 'ignore').decode(), self.rating,
                          self.upc, self.description.encode("ascii", "ignore"), self.price,
                          self.availability, self.num_of_reviews)
