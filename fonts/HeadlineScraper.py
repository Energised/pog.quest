# HeadlineScraper.py
# @author Dan Woolsey
#
# - Have a list of news websites to pull data from
# - Get the top 5/10 popular news articles
# - Pull the headline and summary of each article
# - Put these into a dictionary/json file

from random import randint
import itertools
import requests
#from bs4 import BeautifulSoup
from SoupFactory import SoupFactory

#page = requests.get(websites["bbc"])

#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#print(list(soup.children))

#for p_tag in soup.find_all('p', class_="gs-c-promo-summary"):
#    print(p_tag.get_text())

msn_filter = ["Home", "News", "Weather", "Entertainment", "Sport", "esports",
              "Money", "Lifestyle", "Horoscopes", "Health & Fitness", "Food & Drink",
              "Cars", "Travel", "Dating", "Sponsored:"]

class HeadlineScraper:

    def __init__(self):
        self.headlines = []
        self.headlines_and_taglines = {}
        self.factory = SoupFactory()
        self.scrape_headlines_bbc()
        self.scrape_headlines_msn()
        self.scrape_headlines_huff()

    # only gives headlines, no access to extra content unless i follow the rabbithole
    def scrape_headlines_bbc(self):
        #page = requests.get(self.websites["bbc"])
        soup = self.factory.serve_soup("bbc")
        for p_tag in soup.find_all('p', class_="gs-c-promo-summary"):
            self.headlines.append(p_tag.get_text())

    # as with bbc will only scrape headlines
    # but also has to filter out the crap
    def scrape_headlines_msn(self):
        #page = requests.get(self.websites["msn"])
        soup = self.factory.serve_soup("msn")
        content = soup.find_all('li')
        content_text = []
        for item in content:
            content_text.append(item.get_text())
        filtered = [h for h in content_text if not any(filter in h for filter in msn_filter)]
        tidied = [self.headlines.append(h.strip("\n\r")) for h in filtered]

    # this will return headlines and taglines
    def scrape_headlines_huff(self):
        soup = self.factory.serve_soup("huff")
        # get div where class = card__text
        headline_content = soup.find_all('h2', class_ = "card__headline__text")
        tagline_content = soup.find_all('div', class_ = "card__description")
        zipped = zip(headline_content, tagline_content)
        for h, t in zipped:
            self.headlines_and_taglines[h.get_text()] = t.get_text()

    #todo
    def scrape_headlines_wpost(self):
        soup = self.factory.serve_soup("wpost")
        print(soup.prettify())

    def serve_headline(self):
        h_index = randint(0, len(self.headlines) - 1)
        #print(h_index)
        return self.headlines[h_index]



if __name__ == "__main__":
    scraper = HeadlineScraper()
    print(scraper.serve_headline())
    #scraper.scrape_headlines_bbc()
    #scraper.scrape_headlines_msn()
    #scraper.scrape_headlines_huff()
    #print(*scraper.headlines, sep="\n")
    #for key, value in scraper.headlines_and_taglines.items():
    #    print(key + ": " + value)
