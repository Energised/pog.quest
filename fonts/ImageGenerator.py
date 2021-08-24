# ImageGenerator.py
# @author Dan Woolsey
#
# What I want from this:
#   Select an image from a selection of different images
#   (Winkler, maybe some others...)
#
#   function to serve an image object based on a path (use os)
#   function to generate the draw object
#   function to generate the font object
#   function to build draw.text function onto the image
#       - this will then save the image to img/out/
#       - return the path to this image for use on website

from PIL import Image, ImageFont, ImageDraw

class ImageGenerator:

    def __init__(self):
        # calls to other functions here
        self.im = None
