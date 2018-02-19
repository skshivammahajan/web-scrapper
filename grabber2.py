import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage,"html.parser")
	return soupdata
playaersaved = ""
soup = make_soup("http://www.basketball-reference.com/players/a/")
for record in soup.findAll('tr','a'):
	playerdata = ""
	for data  in record.findAll('td'):
		playerdata = playerdata +"," +data.text
	playaersaved = playaersaved + "\n" + playerdata[1:]

header = "Player,From,To,Pos,Ht,Wt,Birth Date,College"+"\n"
file =open(os.path.expanduser("Basketball.csv"),"wb")
file.write(bytes(header,encoding="ascii",errors='ignore'))
file.write(bytes(playaersaved,encoding="ascii",errors='ignore'))



# import urllib
# import urllib.request
# import os
# from bs4 import BeautifulSoup

# def make_soup(url):
# 	thepage = urllib.request.urlopen(url)
# 	soupdata = BeautifulSoup(thepage,"html.parser")
# 	return soupdata
# playaersaved = ""
# soup = make_soup("http://www.basketball-reference.com/players/a/")
# for record in soup.findAll('tr'):
# 	playerdata = ""
# 	for data  in record.findAll('th'):
# 		for data  in record.findAll('a'):
# 			playerdata = playerdata +"," +data.text
# 	playaersaved = playaersaved + "\n" + playerdata[1:]

# header = "Player,From,To,Pos,Ht,Wt,Birth Date,College"+"\n"
# file =open(os.path.expanduser("Basketball.csv"),"wb")
# file.write(bytes(header,encoding="ascii",errors='ignore'))
# file.write(bytes(playaersaved,encoding="ascii",errors='ignore'))
