from bs4 import BeautifulSoup
import requests


class WebSite:
    """
    Helper class that is used to store a  aBeautifulSoup object and the url from which the BeautifulSoup object
    was created.
    """
    def __init__(self, base_url):
        self.base_url = base_url
        self.bs4_object = BeautifulSoup(requests.get(base_url).text, "html.parser")


