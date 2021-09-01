# pog.quest

This is more of a playground to mess around with some ideas. Current tasks listed below:

## Learning Javascript

### Chapter 2: JS Development Tools

- Using `npm` and installing `underscore`
- Using `gulp`, setting up a `gulpfile` for streamlined build processes in JS

### Chapter 3 : Literals, Variables, Constants and Data Types

- Data types deep dive, most of this I already know so skimmed a lot of this chapter

---

## fonts\

Toolchain to scrape headlines from various news sources, use the Google Fonts API to get a list
of their entire Font catalogue and pull specific font files and bring both of those into a PIL
image to draw the headline onto an image given a font file.

### HeadlineScraper.py and SoupFactory.py

Pulls headline and tagline data from multiple news websites.
Requirements: requests, bs4 (BeautifulSoup)

- [] Add more news websites to the scraper
- [] Read into the bs4 documentation, see what interesting stuff there is

### ImageGenerator.py

To have a string be displayed on top of an image either user defined or pulled from some
web source. Also handles formatting and justification of text to fit within the images size.

- [] Add option for user defined font size
- [] Allow users to choose font family variants

Requirements: pillow (PIL - Python Imaging Library)  

### FontFetch.py

Sends a request to the Google Fonts API to get a list of their entire Font library including URLs
for each font family and variant. It can then pull a given fonts file, store it locally and pass it
to the ImageGenerator.

- [] Create a search system to navigate through the font library data
- [] Create auto-suggestion system for the search

### Planning Steps

- [x] Use Google Fonts API to generate a JSON file containing all font names and URLs for the fonts they host
- [] This can be used for an auto-complete search system on the website to select a font
- [x] Once user has selected a font, we can pull the .ttf file into a PIL.ImageFont object
- [x] This can be used to generate a text image where the text comes from the files in news-scraper/

- [] Build a basic web interface using Flask
- [] Incorporate the fonts\ library into the webpage
- [] Add auto-deletion system for generated images and font files after a given period of time
- [] Look at minimising HeadlineScrapers requests by caching the headlines dict and updating it at certain times
