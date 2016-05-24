from lxml import html
import requests
#from bs4 import BeautifulSoup
import bs4
test = open('test.txt', 'w')

url = 'http://game.thronemaster.net/?game=63100&show=log'

#Get the webpage
page = requests.get('http://game.thronemaster.net/?game=63100&show=log')

soup = bs4.BeautifulSoup(page.text, 'lxml')

#Acquire the content for the entire page
tree = html.fromstring(page.content)

print ('scraping')
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


print ('done scraping')

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)

for player, move, phse in zip(players, moves, phase):
    line = ("" + player + ": " + phse + " MOVE: " + move + '\n ')
    test.write(line)

player = [players[0], players[1], players[2]]
win = [0, 0, 0]


for x in range(0, 3):
    if (players[x] + ' wins this game of thrones!') == moves[len(moves)-1]:
        win[x] = 1

print (win, player)