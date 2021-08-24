# main.py
# @author Dan Woolsey
#
# Bring the classes together and display something cool

from HeadlineScraper import HeadlineScraper
from FontFetch import FontFetch

if __name__ == "__main__":
    scraper = HeadlineScraper()
    font_fetch = FontFetch()
    # setup random headling and font
    random_headline = scraper.serve_random_headline()
    random_font = font_fetch.get_random_ttf()
    print(random_headline)
    print(random_font)