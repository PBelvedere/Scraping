from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib2
test = open('test.txt', 'w')

url = 'http://game.thronemaster.net/?game=63100&show=log'

content = urllib2.urlopen(url).read()
#Get the webpage
page = requests.get('http://game.thronemaster.net/?game=63100&show=log')
soup = BeautifulSoup(content, 'lxml')

#Acquire the content for the entire page
tree = html.fromstring(page.content)

print 'scraping'
#create a list of players
players = []

for plyr in soup.find_all('nobr'):
    players.append(plyr.get_text())
#Create a list of moves
moves = []

for mvs in soup.find_all(id = True):
    moves.append(mvs.get_text())

phase = []

#Find all phases, used a different syntax due to multiple valigns and multiple small tags
phase = tree.xpath('//th[@valign = "top"]/small/text()')


print 'done scraping'



for player, move, phse in zip(players, moves, phase):
    print>>test, player, ': ', phse, ' MOVE: ', move, '\n '

