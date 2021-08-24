# FontFetch.py
# @author Dan Woolsey
#
# This will:
# - Contact Google API, request all font data
# - Extract family, styles and urls
# - Allow you to search through its font db
#   - will match your search term to its font names
#   - return the top 5 results along with their styles
# - Given the font name and a style, return the a ttf filename
#   - this is where the font will be cached locally in fonts/
#   - then the file name with the 'font/' prefix will be returned
#   - this way it can be passed directly into an ImageFont object

from functools import lru_cache
from random import randint

import constants as c
import requests
import urllib.request as u_req

class FontFetch:

    def __init__(self):
        fonts_page = requests.get(c.GFONTS_URL)
        fonts_json = fonts_page.json()
        self.fonts_list = fonts_json["items"]
        self.fonts_dict = {}
        for font_dict in self.fonts_list:
            #print(font_dict["family"])
            #print(font_dict["variants"])
            #print(font_dict["files"])
            self.fonts_dict[font_dict["family"]] = font_dict["files"]

    @lru_cache
    def get_ttf(self, family, variant):
        font_url = self.fonts_dict[family][variant]
        file_name = (family.replace(" ", "_") + "_" + variant + ".ttf").lower()
        file_path = c.FONT_DIR + file_name
        #print(file_path)
        u_req.urlretrieve(font_url, file_path)
        return file_path

    def get_random_ttf(self):
        font_family_index = randint(0, len(self.fonts_dict)-1)
        random_font_name = list(self.fonts_dict)[font_family_index]
        #print(self.fonts_dict[random_font_name])
        font_variant_index = randint(0, len(self.fonts_dict[random_font_name])-1)
        #print(font_variant_index)
        random_font_variant = list(self.fonts_dict[random_font_name])[font_variant_index]
        #print(random_font_name)
        #print(random_font_variant)
        return self.get_ttf(random_font_name, random_font_variant)

    def search_test(self, family, variant = ""):
        if family in self.fonts_dict:
            print(self.fonts_dict[family])

if __name__ == "__main__":
    x = FontFetch()
    #x.search_test("Zen Loop")
    font_1_path = x.get_ttf("Zen Loop", "regular")
    random_font_url = x.get_random_ttf()
