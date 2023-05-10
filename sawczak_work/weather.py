# To use this, you'll need to run these commands in the terminal:

# pip install beautifulsoup4
# pip install requests

# You may have to write pip3 or pip3.10 or pip3.11 instead

from bs4 import BeautifulSoup
import requests

def get_celsius_toronto() -> int:

    # Let's get the CBC current weather page for Toronto
    url = 'https://www.cbc.ca/weather/s0000458.html'
    html = requests.get(url).text

    # Parse the HTML into a "soup" of data
    # See documentation here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    soup = BeautifulSoup(html, 'html.parser')

    # Now the tedious part of navigating an HTML structure unique to each page.
    # I had to inspect the HTML by hand to identify its structure, but once I have
    # the 'ltemp' & 'celsius' identifiers, I could use this script to automatically
    # pull the current Celsius in Toronto in future.

    temp_tag = soup.find(id='ltemp')
    celsius_tag = temp_tag.find(class_='celsius')
    celsius_text = celsius_tag.get_text().strip()
    celsius = int(celsius_text.split('°')[0])

    return celsius

if __name__ == '__main__':
    print(get_celsius_toronto())
