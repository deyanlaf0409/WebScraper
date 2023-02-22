MAX_BOOKS = 1000
from Filter.Filter import Filter
from Sorting.sorting import Sorter
from Arg_Parser.arg_parser import VALID_SORTINGS


def validate_num_of_books(num):
    """
    This function checks and validates the number coming from the number of books textbox.
    :param num: The num taken from the number of books field.
    :return: The int format of the given number, or 1000 if the num is above 1000.
    """
    if not num: return 1000
    else:
        num = num.strip()
        if not num.isdigit():
            raise Exception("Number of books should be an integer")
        elif int(num) > MAX_BOOKS:
            print "Number exceeds maximum number of books, searching for max amount instead."
            return 1000
        else:
            return int(num)


def create_filters(gui_list, filter):
    """
    This function creates the filters taken from the filter textbox.
    :param gui_list: This is the filters taken as a list from the textbox.
    :param filter: The current filter.
    """
    if not all(gui_list): return None
    for i in gui_list:
        if "rating" in i: filter.rating_filter = i
        elif "available" in i: filter.availability_filter = i
        elif "unique" in i: filter.upc_filter = i
        elif "price" in i: filter.price_filter = i
        elif "reviews" in i: filter.num_of_reviews = i
        else: print "filter {0} not viable and will thus be skipped".format(i)


def validate_sorting_criterias(sorters_list):
    """
    This function validates the sorting request from the user.
    :param sorters_list: The list of attributes to sort through.
    :return: Returns a sorted list of items.
    """
    if not all(sorters_list): return None
    sorters_list = [item.strip() for item in sorters_list]
    for i in sorters_list:
        if i not in VALID_SORTINGS:
            raise Exception("Invalid sorting criteria. List of viable criterias: {0}".format(VALID_SORTINGS))

    return sorters_list
