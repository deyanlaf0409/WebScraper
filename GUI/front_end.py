import Tkinter as tk
from validate__input_gui import *

# mapped list of text we need for our labels
list_of_labels = [
    "Number of books:",
    "Enter genres:",
    "Enter a list of filters:",
    "Enter a list of keywords to search for in the description:",
    "Enter JSON file name with titles (file must be in project root directory):",
    "Enter a list of sortings:"
]


def create_window(title):
    """
    Creates a tkinter window
    :param title: text of tkinter window
    :return: tkinter window
    """
    window_app = tk.Tk()
    window_app.title(title)
    window_app.minsize(width=600, height=600)
    return window_app


def textbox_generator(label, height, width, window):
    """
    generates one textbox
    :param label: text in label of our textbox
    :param height: height of our textbox
    :param width: width of our textbox
    :param window: window where our textbox will be
    :return: our tkinter textbox
    """
    generated_textbox_label = tk.Label(window, text=label).pack()
    generated_textbox = tk.Text(window, height=height, width=width)
    generated_textbox.pack()
    tk.Text(generated_textbox).insert(tk.END, "")
    return generated_textbox


def generate_textboxes(window):
    """
    wrapper function that generates however many textboxes we need/(are mapped in list_of_labels)
    :param window: window for our textboxes
    :return: list of our textboxes
    """
    return [textbox_generator(textbox, 2, 30, window) for textbox in list_of_labels]


def create_menu(text_of_menu):
    """
    creates a tkinter menu with text of our choice
    :param text_of_menu: text for our tkinter menu
    :return: tkinter menu
    """
    menu = tk.StringVar()
    menu.set(text_of_menu)
    return menu


def create_dropdown_menu(options, window_app, menu):
    """
    creates a tkinter dropdown menu with specific options
    :param options: options that we want our menu to have
    :param window_app: window for our menu
    :param menu: menu that will house our options
    :return: tkinter dropdown menu
    """
    order_choice = tk.StringVar()
    drop = tk.OptionMenu(window_app, menu, *options)
    drop.pack()
    return drop


def create_button(frame, func, text_of_button):
    """

    :param frame: window that will house our button
    :param func: function that will be executed upon pressing the button
    :param text_of_button: text of our button
    :return: tkinter button
    """
    button_info = tk.Button(frame, text=text_of_button, fg="red", command=func)
    button_info.pack()
    return button_info


class Gui:
    """
    this is our gui class that creates a window with the necessary buttons and menus
    
    """
    def __init__(self, text="Book Scraper CodeAcademy"):
        self.window = create_window(text)
        self.top_frame = tk.Frame(self.window).pack()
        self.bottom_frame = tk.Frame(self.window).pack(side="bottom")
        self.label = tk.Label(self.window, text="Welcome to Book Scraper app").pack()
        self.textboxes = generate_textboxes(self.window)
        self.menu = create_menu("Select sorting direction, default is Descending")
        self.dropdown_menu = create_dropdown_menu(["Sorting - Ascending", "Sorting - Descending"],
                                                  self.window, self.menu)
        self.search_button = create_button(self.top_frame, self.start_searching, "Searching")
        self.filter = Filter()
        self.sorter = Sorter()
        self.filter.num_of_books = "gui premature exit" #ako cuknem search shte se overwritne, ako ne
        #toest ako sme mahnali guito s x shte flagne che programata trqbva da se spre
        self.window.mainloop()

    def start_searching(self):
        """
        method that will execute upon pressing the Search button, it will collect user input and redirect
        it to Filter and Scraper class instances
        :return: 
        """
        self.filter.num_of_books = validate_num_of_books(self.textboxes[0].get("1.0", "end-1c"))
        self.filter.genres = [str(genres.replace(",", "").strip()) for genres in self.textboxes[1].get("1.0", "end-1c").split(",") ]\
            if self.textboxes[1].get("1.0", "end-1c") else None
        create_filters(self.textboxes[2].get("1.0", "end-1c").split(","), self.filter)
        self.filter.words_in_description = self.textboxes[3].get("1.0", "end-1c")
        self.filter.words_in_title = self.textboxes[4].get("1.0", "end-1c")
        self.sorter.filter = validate_sorting_criterias(self.textboxes[5].get("1.0", "end-1c").split(","))
        self.sorter.order = "ascending" if self.menu.get() == "Sorting - Ascending" else "descending"
        self.window.destroy()
