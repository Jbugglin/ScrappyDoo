import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.amazon.com/s?k=disc+golf+discs&crid=1IXKAE9NWIIYO&sprefix=disc+golf+discs%2Caps%2C93&ref=nb_sb_noss_1"
page = requests.get(url)

html = BeautifulSoup(page.content, "html.parser")
status = page.status_code
print(status)


