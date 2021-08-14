# textImageGen.py
# @author Dan Woolsey
#
# - Convert text into an image file where font is a variable

from PIL import Image

im = Image.open("img/winkler-stage-hands.jpg")

print(im.format, im.size, im.mode)
im.show()
