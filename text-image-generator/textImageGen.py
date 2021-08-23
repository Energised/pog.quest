# textImageGen.py
# @author Dan Woolsey
#
# - Convert text into an image file where font is a variable

import ast
import requests

import urllib.request

from PIL import Image, ImageFont, ImageDraw

im = Image.open("img/winkler-stage-hands.jpg")
im_crop = Image.open("img/winkler-cut-2.png")

draw = ImageDraw.Draw(im)

# setup for website, so won't work locally
# will generate a new one for local use that I won't keep here
# since exposing an API key unrestricted could be v bad

API_KEY = "AIzaSyDAPrRgrQj9Pw9igcKD2boWBTfBBhBzIU8"

GFONTS_URL = "https://www.googleapis.com/webfonts/v1/webfonts?key=%s" % (API_KEY)

font_name_url = {}

page = requests.get(GFONTS_URL)

json_response = page.json()

fonts_list = json_response["items"]
#single_font_dict = fonts_list[0]
#print(single_font_dict["family"]) # pulls single font name

for font_dict in fonts_list: # unpack list of dictionaries
    #print(font_dict["family"]) # here we can access keys from the json
    font_name_url[font_dict["family"]] = font_dict["files"]
    #print(font_dict["files"]["regular"])
    #print(font_dict["files"].keys())

# for key, value in font_name_url.items():
#     print(str(key + ":"))
#     for type, url in value.items():
#         print(type + " -> " + url)

# we now have font_name_url as:
# {font_name : {font_style_1 : url, font_style_2 : url, ...}, ...}

test_url = font_name_url["Acme"]["regular"]

urllib.request.urlretrieve(test_url, "acme.ttf")
print("download done")

tt_font = ImageFont.truetype("acme.ttf", 70)

draw.text((200, 300), "Back at it!", font=tt_font, fill="black")

im.show()

#with open("font-request.txt", "w") as file:
#    for key, value in json_response.items():
#        for item in value:
#            #print(items_dict.keys())
#            file.write(str(item) + "\n")

print(im_crop.format, im_crop.size, im_crop.mode)
#im_crop.show()
