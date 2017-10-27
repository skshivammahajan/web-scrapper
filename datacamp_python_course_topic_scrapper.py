# import libraries
from urllib import request
from bs4 import BeautifulSoup
# specify the url
quote_page = 'https://www.datacamp.com/courses/tech:python'
# query the website and return the html to the variable page
page = request.urlopen(quote_page)
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# Now we have a variable, soup, containing the HTML of the page
name_box = soup.find_all("h4", attrs={"class": "course-block__title"})
# h1 is html tag and name is class for that tag
titles = list()
for name in name_box:
	title = name.text.strip() # strip() is used to remove starting and trailing
	titles.append(title)
# Saving the data in a excel file
import csv
from datetime import datetime
# open a csv file with append, so old data will not be erased
with open('datacamp_python_courses.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	for heading in titles:
		writer.writerow([heading])

