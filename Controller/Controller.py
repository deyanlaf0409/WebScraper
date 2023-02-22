import json
import sys
from Arg_Parser.arg_parser import *
from Scraping.scraper import Scraper
from Sorting.sorting import Sorter


def output(current_book):
    """
    This method outputs the final result to a .json file.
    :param current_book: the book to be saved to the file.
    """
    with open("output.json", "w+") as custom_file:
        def obj_dict(obj):
            return obj.__dict__

        json_string = json.dumps(current_book, indent=4, default=obj_dict, ensure_ascii=True)
        custom_file.write(json_string)


class Controller:
    """
    This class takes command line arguments and pass it to the class methods.

    Method:
    - output
    - start_gui
    - start_without_gui
    - decide_where_to_start
    """

    def __init__(self):
        pass

    def start_gui(self):
        """
        This method starts the program with GUI (graphical user interface)

        """
        from GUI.front_end import Gui
        gui = Gui()
        scraper = Scraper(gui.filter)
        sorter = gui.sorter
        print "Scraping started. Please wait."
        list_of_books = scraper.get_books_info()
        if gui.sorter.filter is not None:
            list_of_books = sorter.sort_books(list_of_books)
        output(list_of_books)
        if list_of_books:
            for i in list_of_books:
                print i
        else: print "No books found."



    def start_without_gui(self, cmd_args):
        """
        This method starts the program without the GUI.
        :param cmd_args: the arguments from the command line.
        """
        scraper = Scraper()
        print "Scraping started. Please wait."
        list_of_books = scraper.get_books_info()
        if cmd_args.list_of_sortings:
            sorter = Sorter(cmd_args.list_of_sortings, cmd_args.list_of_sortings[-1])
            list_of_books = sorter.sort_books(list_of_books)
        output(list_of_books)
        if list_of_books:
            for i in list_of_books:
                print i
        else: print "No books found."


    def decide_where_to_start(self, result_from_argparser=None):
        """
        This method helps the program decide where to start depending on if the "-X" argument is present.
        :param result_from_argparser: the parsed arguments from the command line.
        """
        a = Arg_Parser()
        if a.gui_boolean and len(sys.argv) <= 2:
            self.start_gui()
        else:
            self.start_without_gui(a)



