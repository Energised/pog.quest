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

    def __init__(self, font_path, headline):
        # calls to other functions here
        self.im = self.get_image("img\winkler-stage-hands-top-banner.png")
        self.draw = self.get_draw_obj()
        self.font = self.get_font_obj(font_path)
        self.generate_text_on_image(headline)

    def get_image(self, path):
        im = Image.open(path)
        return im

    def get_draw_obj(self):
        draw = ImageDraw.Draw(self.im)
        return draw

    def get_font_obj(self, font_path):
        tt_font = ImageFont.truetype(font_path, 28)
        return tt_font

    # currently this will be hardcoded for one image
    # so position of text and fill colour are pre-set
    def generate_text_on_image(self, headline):
        self.draw.text((20,0), headline, font=self.font, fill="black")

    def display(self):
        self.im.show()
