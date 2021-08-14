# SoupFactory.py
# @author Dan Woolsey
#

from bs4 import BeautifulSoup

class SoupFactory(BeautifulSoup):

    def __init__(self, *args):
        super().__init__(*args)
