import csv
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.geeksforgeeks.org/java-projects/") #replace this url with one that will be generalized. 

soup = BeautifulSoup(page.content, 'html.parser') #standard soup declaration.
projectName = [] #initialize the array to send the h3 elements.
for i in soup.find_all('h3'): #finds all h3 elements on the page.
    header3Name = i.text #setting the incoming data to string. 
    projectName.append(header3Name.strip()) #creating the excel file header.


file_name = 'scrapedHeaders3.csv'
with open(file_name, 'w', encoding='utf-8') as f:
    f.write = csv.writer(f)
    f.write.writerow(['projectName']) #the header of the excel file

    #For loop cycles through the array of h3's and prints out on each row in the excel file. 
    for i in range(len(projectName)):
        f.write.writerow([i+1, projectName[i]])

# Note 1. This works to pull the h3 elements off of the page. 
        # Note 2. I want to create a cheat sheet of sorts, to be able to just comment out what needs scraped. 

        # Note 3. I want to scrape TCG price data and be able to utilize excel to follow card prices. When they dip and when they rise. For science of course.