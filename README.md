# S04-Python-team-5
# Documentation:

This is a plan of the idea and main structure of the project.

1.Web scraping from http://books.toscrape.com
 - getting the proper n books depending on the input and collect them in a chosen data structure

2.Filter the data depending on the input:
- data is sorted depending on the input
- store formatted data in json

3.Output the data in tkinter

# Project Requirements:
- Python 2.7
- Modules : argparse, requests, beautifulsoup, tkinter

Project content:
- Tests, documentation, OOP design, UML diagram

Optional input arguments:
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
...

# UML Diagram:
![classes](https://user-images.githubusercontent.com/111605228/220118325-117f397a-8753-4e29-a264-e3ac94608435.png)







