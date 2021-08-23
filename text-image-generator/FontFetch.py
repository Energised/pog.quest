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

class FontFetch:
    
