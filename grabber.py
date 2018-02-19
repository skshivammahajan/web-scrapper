import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage,"html.parser")
	return soupdata
a=2000000000
b=9999999999
for i in range(a,b):	
	phone=str(i)
	print ("https://thatsthem.com/phone/"+phone)
	playaersaved = ""
	soup = make_soup("https://thatsthem.com/phone/"+phone)
	for record in soup.findAll('ul'):
		playerdata = ""
		for data  in record.findAll('h3'):
			for data2  in data.findAll('span'):
				# for data3 in data2.findAll('itemprop'):
				playerdata = playerdata +"," +data2.text
		if len(playerdata)!=0:		
			playaersaved = playaersaved + "\n" + playerdata[1:]

	header = "Player,From,To,Pos,Ht,Wt,Birth Date,College"+"\n"
	file =open(os.path.expanduser("Basketball.csv"),"wb")
	file.write(bytes(header,encoding="ascii",errors='ignore'))
	file.write(bytes(playaersaved,encoding="ascii",errors='ignore'))
