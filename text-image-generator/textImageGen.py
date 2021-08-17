# textImageGen.py
# @author Dan Woolsey
#
# - Convert text into an image file where font is a variable

import ast
import requests

from PIL import Image

API_KEY = "AIzaSyDAPrRgrQj9Pw9igcKD2boWBTfBBhBzIU8"

GFONTS_URL = "https://www.googleapis.com/webfonts/v1/webfonts?key=%s" % (API_KEY)

page = requests.get(GFONTS_URL)

json_response = page.json()

fonts_list = json_response["items"]
#single_font_dict = fonts_list[0]
#print(single_font_dict["family"]) # pulls single font name

for font_dict in fonts_list: # unpack list of dictionaries
    print(font_dict["family"]) # here we can access keys from the json


with open("font-request.txt", "w") as file:
    for key, value in json_response.items():
        for item in value:
            #print(items_dict.keys())
            file.write(str(item) + "\n")


im = Image.open("img/winkler-stage-hands.jpg")
im_crop = Image.open("img/winkler-cut-2.png")

print(im_crop.format, im_crop.size, im_crop.mode)
#im_crop.show()
