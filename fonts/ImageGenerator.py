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
# - having now found the image_utils class on Github
#   - think I will subclass this and add in extra functions
#
#
#


from image_utils import ImageText
from PIL import Image, ImageFont, ImageDraw

import constants as c

class ImageGenerator:

    def __init__(self, font_path, font_size_pt, headline):
        # calls to other functions here
        self.im = self.get_image("img\winkler-stage-hands-top-banner.png")
        self.im_width, self.im_height = self.im.size
        self.font_size_pt = font_size_pt
        self.draw = self.get_draw_obj()
        self.font = self.get_font_obj(font_path)
        self.headline = headline
        self.lines = self.generate_lines()
        self.generate_text_on_image(headline)

    def get_image(self, path):
        im = Image.open(path)
        return im

    def get_draw_obj(self):
        draw = ImageDraw.Draw(self.im)
        return draw

    def get_font_obj(self, font_path):
        tt_font = ImageFont.truetype(font_path, self.font_size_pt)
        return tt_font

    def generate_lines(self, padding=20):
        words = [w for w in self.headline.split(" ") if w]
        chars = [c for c in self.headline]
        total_chars = len(chars)
        print("total_chars = " + str(total_chars))
        print(words)
        # number of pixels in width and height of 1 character
        font_pixel_width = self.font_size_pt * c.POINT_PX_CR
        max_chars_per_line = round((self.im_width - padding) / font_pixel_width)
        print("max_chars_per_line = " + str(max_chars_per_line))

        lines = []
        ptr = max_chars_per_line
        last_ptr = 0
        #print("ptr=" + str(ptr))
        print("total_chars=" + str(total_chars))
        while ptr <= total_chars:
            print("ptr=" + str(ptr))
            if chars[ptr] == " ":
                lines.append(''.join(str(e) for e in chars[last_ptr:ptr]))
            else:
                while chars[ptr] != " ":
                    ptr -= 1;
                    print(ptr)
                    print(chars[ptr])
                lines.append(''.join(str(e) for e in chars[last_ptr:ptr]))
            last_ptr = ptr + 1
            ptr += max_chars_per_line
        lines.append(''.join(str(e) for e in chars[last_ptr:total_chars]))

        print(lines)
        return lines


    # currently this will be hardcoded for one image
    # so position of text and fill colour are pre-set
    def generate_text_on_image(self, headline):
        self.draw.text((20,0), headline, font=self.font, fill="black")

    def display(self):
        self.im.show()

if __name__ == "__main__":
    x = ImageGenerator("fonts/alike_regular.ttf", 28, "Boris Johnson has shat himself... again.")
    x.generate_lines()
