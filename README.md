# S04-Python-team-5
This project is made by me and my 3 comrades throughout our coding bootcamp.
Not perfect, but it covers the main requierments which are:

                                                       - OOP Design
                                                       
                                                       - Tests cover around 75%
                                                       
                                                       - Works as expected
                                                       
# What it does?
Scrapes books info from "http://books.toscrape.com" and saves that info in readable format as json file.

You can add some arguments depending on what are you searching for (price range, title, rating etc.) or just "gonna catch 'em all!" (Which i don't recommend).

Add -X as argument for Graphical User Interface (This sounds cooler than it looks).

Look for quick instructions below.


# Project Requirements:
- Python 2.7
- Modules : argparse, requests, beautifulsoup, tkinter

#Optional input arguments:
```
  -h, --help          show this help message and exit
  -d, --description   description keywords
  -g, --genre         genre
  -f, --filter        filter
  -n, --number        number of books
  -t, --title         book title
  -F, --json          <filename>.json5
  -s, --sort          sort (ascending/descending)
  -X, --gui           graphical user interface
  ```

# Example input:
python main.py -b 50 -g Science -s rating ascending

python main.py -b 24 -g Classics -f “rating < 3”

python main.py -b 60 -g Science -f “available =14, rating < 3” -d “book, person, car”

python main.py -g Science -t “Book Title”

python main.py -X

# Tests
In main directory 







