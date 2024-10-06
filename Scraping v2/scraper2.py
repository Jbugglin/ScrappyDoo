import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://learntocodewith.me/posts/portfolio-tips/#what-to-include-in-a-portfolio"
page = requests.get(url)

html = BeautifulSoup(page.content, "html.parser")
status = page.status_code
print(status)


