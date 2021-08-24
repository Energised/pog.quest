# SoupFactory.py
# @author Dan Woolsey
#
# Had the drunken idea of a SoupFactory that generated soup based on the
# website I pass in - e.i the keys of the websites dict in scraper.py
#
# BeautifulSoup(document, parser) - document can be any text
#                                 - parsers built in for many languages
#
# SoupFactory("bbc") - Could take as its only argument the news site we're looking for
#                    - Then we generate document via a method call in the constructor
#                    - Then pass the doc and an html parser into the super constructor
#
# ^^ above idea doesn't allow me to return the soup, so have made serve_soup("bbc")
#    which does the exact same thing and makes this more like the factory design pattern

import requests
from bs4 import BeautifulSoup

class SoupFactory():

    websites = {"bbc" : "https://www.bbc.co.uk/news/uk",
                "msn" : "https://www.msn.com/en-gb/",
                "huff" : "https://www.huffingtonpost.co.uk/news/",
                "wpost" : "https://www.washingtonpost.com/"}

    head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

    # todo: decide what I would use a constructor for in here

    def serve_soup(self, site_name):
        self.site_url = self.websites[site_name]
        # temp workabout since using self.head with msn breaks my filter
        if(site_name == "msn"):
            self.page = requests.get(self.site_url)
        else:
            self.page = requests.get(self.site_url, headers=self.head)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        return self.soup
