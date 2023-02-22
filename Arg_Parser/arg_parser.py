import argparse

"""
b - number of books

g - list of genres to search through 

s - list of sortings {ascending , descending}

f - list of filters

d - list of keywords for searching in the description  -> "people, cars, cats"

t - search for a book by title 

F - list of book titles to search for (from given json)

X - GUI
"""


def range_type(num_to_check, min=1, max=1000):
    '''
    Custom type so we get a prettier error if we enter an invalid number of books
    :param num_to_check: number we are checking
    :param min: min number of books you can scrape
    :param max: max number of books you can scrape
    :return: number of books if valid, else raises TypeError
    '''
    value = int(num_to_check)
    if min<= value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError('value not in range %s-%s'%(min,max))

#mapping of valid filters so we could easily loop over them for validation purposes
VALID_FILTERS  = ["rating", "available", "unique", "price", "reviews"]
#mapping of valid sortings so we could easily loop over them for validation purposes
VALID_SORTINGS = ["rating", "review", "reviews", "description", "upc", "availability", "name",
                  "ascending", "descending", "price"]


class Arg_Parser:
    __argparser = argparse.ArgumentParser()
    __argparser.add_argument("-b", type=range_type, help="number of books")
    __argparser.add_argument("-g", type=str, help="list of genres to search through", nargs="*")
    # v neta ne uspqh da namerq kak da naprava separatora da e , vmesto space taka che ganrovete shte trqbva da se
    # vkarvat kato stringove aka vseki genre trqbva da e otdelen string :(
    __argparser.add_argument("-s", help="list of sortings {ascending , descending}",
                            type=str)
    __argparser.add_argument("-f", type=str, help="list of filters")
    __argparser.add_argument("-d", type=str, help="list of keywords to search for")
    __argparser.add_argument("-t", type=str, help="search title book")
    __argparser.add_argument("-F", type=str, help="list of book titles")
    # check the below line for errors later, as we need to modify it seperately
    __argparser.add_argument("-X", help="GUI activation", action="store_true")


    '''
    Wrapper class for parsed command line arguments
    '''
    def __init__(self):
        self.args = self.__argparser.parse_args()
        self.num_of_books = self.args.b if self.args.b else ""
        self.list_of_genres = [genre.replace(",", "") for genre in self.args.g] if self.args.g else ""
        self.list_of_sortings = [item.strip() for item in self.args.s.split(",")] if self.args.s else ""
        self.__list_of_filters = self.args.f.split(",") if self.args.f else ""
        self.rating = ""
        self.availability = ""
        self.upc = ""
        self.price = ""
        self.num_of_reviews = ""
        self.__create_filters()
        self.list_of_keywords = self.args.d if self.args.d else ""
        self.search_title_book = self.args.t if self.args.t else ""
        self.list_of_titles = self.args.F if self.args.F else ""
        self.gui_boolean = self.args.X if self.args.X else ""

    def __create_filters(self):
        '''
        creates numerous filters from a list given to us by command line
        '''
        if self.__list_of_filters:
            for i in self.__list_of_filters:
                if "rating" in i: self.rating = i
                elif "available" in i: self.availability = i
                elif "unique" in i: self.upc = i
                elif "price" in i: self.price = i
                elif "reviews" in i: self.num_of_reviews = i
                else: print "filter {0} not applicable and thus will be skipped.\nlist of valid filters:{1}".format(i, VALID_FILTERS)

