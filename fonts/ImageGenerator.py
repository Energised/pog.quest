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
#
# image_utils just wasn't working so i'm building it myself
#
#

from datetime import datetime
from PIL import Image, ImageFont, ImageDraw

import string
import random

import constants as c

class ImageGenerator:

    def __init__(self, font_path, font_size_pt, headline):
        # calls to other functions here
        self.im = self.get_image("img\winkler-stage-hands-top-banner.png")
        self.im_width, self.im_height = self.im.size
        self.font_path = font_path
        self.font_size_pt = font_size_pt
        self.draw = self.get_draw_obj()
        self.font = self.get_font_obj(font_path)
        self.headline = headline
        self.lines = self.generate_lines()
        #self.generate_text_on_image(headline)
        self.draw_text_on_image("center")
        self.save()

    def get_image(self, path):
        im = Image.open(path)
        return im

    def get_draw_obj(self):
        draw = ImageDraw.Draw(self.im)
        return draw

    def get_font_obj(self, font_path):
        tt_font = ImageFont.truetype(font_path, self.font_size_pt)
        return tt_font

    # much smaller and easier way to generate lines
    # using font.getsize and overriding the char list
    def generate_lines(self, padding=20):
        chars = [c for c in self.headline]
        total_chars = len(chars)
        lines = []
        ptr = 0
        while ptr <= total_chars:
            total_width = 0
            for char in chars:
                if(total_width >= (self.im_width - padding)):
                    while chars[ptr] != " ":
                        ptr -= 1
                    lines.append(''.join(str(e) for e in chars[:ptr]))
                    chars = chars[ptr:]
                    break
                total_width += self.font.getsize(char)[0]
                ptr += 1
        lines.append(''.join(str(e) for e in chars[:total_chars]))
        return lines

    def draw_text_on_image(self, justify, padding=20):
        # justify could be either 'left', 'right', 'center'
        #font_pixel_size = self.font_size_pt * c.POINT_PX_CR
        start_x, start_y = 0, 0
        for counter, line in enumerate(self.lines):
            font_pixel_width, font_pixel_height = self.font.getsize(line)
            if justify == "center":
                start_x = (self.im_width/2) - ((font_pixel_width)/2)
            elif justify == "left":
                start_x = padding
            elif justify == "right":
                start_x = self.im_width - (font_pixel_width + padding)
            start_y = (font_pixel_height * counter) + padding
            self.draw.text((start_x, start_y), line, font=self.font, fill="black")

    # currently this will be hardcoded for one image
    # so position of text and fill colour are pre-set
    def generate_text_on_image(self, headline):
        self.draw.text((20,0), headline, font=self.font, fill="black")

    def display(self):
        self.im.show()

    def save(self, name=None):
        if name == None:
            name = self.generate_filename()
        self.im.save(name)

    def generate_filename(self):
        date_time = datetime.now()
        formatted_date_time = date_time.strftime("%y-%m-%d-%H-%M-%S-")
        random_string = ''.join([random.choice(string.ascii_lowercase) for _ in range(10)])
        full_img_path = "out/" + formatted_date_time + random_string + ".png"
        return full_img_path

if __name__ == "__main__":
    x = ImageGenerator("fonts/caveat_600.ttf", 28, " The true nature of a disguised mobile telecommunications device is the order of business for today would you believe")
    x.display()



"""
- original generate lines method to remove
def generate_lines(self, padding=20):
    words = [w for w in self.headline.split(" ") if w]
    chars = [c for c in self.headline]
    total_chars = len(chars)
    # number of pixels in width and height of 1 character
    #font_pixel_width = round(self.font_size_pt * c.POINT_PX_CR)
    font_pixel_width = self.font.getsize("a")[0]
    max_chars_per_line = round((self.im_width - padding) / font_pixel_width)
    print(self.im_width)
    lines = []
    ptr = max_chars_per_line
    last_ptr = 0
    while ptr <= total_chars:
        if chars[ptr] == " ":
            lines.append(''.join(str(e) for e in chars[last_ptr:ptr]))
        else:
            while chars[ptr] != " ":
                ptr -= 1;
            lines.append(''.join(str(e) for e in chars[last_ptr:ptr]))
        last_ptr = ptr + 1
        ptr += max_chars_per_line
    lines.append(''.join(str(e) for e in chars[last_ptr:total_chars]))
    return lines

"""
