# pog.quest

This is more of a playground to mess around with some ideas. Current tasks listed below:

## Tasks

- Find more sites to add to SoupFactory
- Pull out headline and tagline info for wpost
- See about requesting fonts directly from fonts.google.com
- Look at overlaying one image onto another in PIL

## Learning Javascript

### Chapter 2: JS Development Tools

- Using `npm` and installing `underscore`
- Using `gulp`, setting up a `gulpfile` for streamlined build processes in JS

### Chapter 3 : Literals, Variables, Constants and Data Types

- Data types deep dive, most of this I already know so skimmed a lot of this chapter


## news-scraper

Purpose: To pull headline and tagline data from multiple news websites for later processing
Requirements: requests, bs4 (BeautifulSoup)

## img-processor

Purpose: To have a string be displayed on top of another image with a random font either taken
from inside PIL or from fonts.google.com

Requirements: pillow (PIL - Python Imaging Library)  

### Planning Steps

- Use Google Fonts API to generate a JSON file containing all font names and URLs for the fonts they host
- This can be used for an auto-complete search system on the website to select a font
- Once user has selected a font, we can pull the .ttf file into a PIL.ImageFont object
- This can be used to generate a text image where the text comes from the files in news-scraper/
- At this point, I don't know exactly how I can do this but here's what I want:
  - Bring the cut image of Henry Winkler into PIL
  - Insert the text image onto the Winkler picture in the appropriate position
  - Export this new image to an output folder
