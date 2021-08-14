# scraper.py
# @author Dan Woolsey
#
# - Have a list of news websites to pull data from
# - Get the top 5/10 popular news articles
# - Pull the headline and summary of each article
# - Put these into a dictionary/json file

import requests
#from bs4 import BeautifulSoup
from SoupFactory import SoupFactory

#websites = {"bbc" : "https://www.bbc.co.uk/news/uk",
#            "vice" : ""}

#page = requests.get(websites["bbc"])

#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#print(list(soup.children))

#for p_tag in soup.find_all('p', class_="gs-c-promo-summary"):
#    print(p_tag.get_text())

websites = {"bbc" : "https://www.bbc.co.uk/news/uk",
            "msn" : "https://www.msn.com/en-gb/"}

msn_filter = ["Home", "News", "Weather", "Entertainment", "Sport", "esports",
              "Money", "Lifestyle", "Horoscopes", "Health & Fitness", "Food & Drink",
              "Cars", "Travel", "Dating", "Sponsored:"]

class HeadlineScraper:

    def __init__(self):
        self.headlines = [];
        self.websites = {"bbc" : "https://www.bbc.co.uk/news/uk",
                         "msn" : "https://www.msn.com/en-gb/",
                         "huff" : "https://www.huffingtonpost.co.uk/news/"}

    # only gives headlines, no access to extra content unless i follow the rabbithole
    def scrape_headlines_bbc(self):
        page = requests.get(self.websites["bbc"])
        soup = SoupFactory(page.content, 'html.parser')
        for p_tag in soup.find_all('p', class_="gs-c-promo-summary"):
            self.headlines.append(p_tag.get_text())

    # as with bbc will only scrape headlines
    # but also has to filter out the crap
    def scrape_headlines_msn(self):
        page = requests.get(self.websites["msn"])
        soup = SoupFactory(page.content, 'html.parser')
        content = soup.find_all('li')
        content_text = []
        for item in content:
            content_text.append(item.get_text())
        filtered = [h for h in content_text if not any(filter in h for filter in msn_filter)]
        tidied = [self.headlines.append(h.strip("\n\r")) for h in filtered]

    def scrape_headlines_huff(self):
        page = requests.get(self.websites["huff"])
        soup = SoupFactory(page.content, 'html.parser')
        print(soup.prettify())


if __name__ == "__main__":
    scraper = HeadlineScraper()
    scraper.scrape_headlines_bbc()
    scraper.scrape_headlines_msn()
    print(*scraper.headlines, sep="\n")
    #scraper.scrape_headlines_huff()
