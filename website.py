"""
import webbrowser as wb
text = input("Search: ")
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
f_text='https://www.google.cl/search?q=' + text
wb.get(chrome_path).open(f_text)
"""

# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup

url = "https://www.virustotal.com/gui/home/url"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

i = soup.div[""]
print(i)